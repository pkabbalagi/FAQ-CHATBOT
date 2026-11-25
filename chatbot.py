import json
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:
    def __init__(self, faq_path, confidence_threshold=0.35):
        self.confidence_threshold = confidence_threshold
        self.faqs = self._load_faqs(faq_path)
        self.stopwords = {
            "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
            "how", "i", "in", "is", "it", "of", "on", "or", "please", "the",
            "to", "what", "when", "where", "which", "who", "with", "you", "your"
        }

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        if self.faqs:
            faq_texts = [
                self.preprocess(
                    faq["question"] + " " + " ".join(faq.get("keywords", []))
                )
                for faq in self.faqs
            ]
            self.faq_matrix = self.vectorizer.fit_transform(faq_texts)
        else:
            self.faq_matrix = None

    @staticmethod
    def _load_faqs(path):
        with open(path, "r", encoding="utf-8") as file:
            faqs = json.load(file)
        if not isinstance(faqs, list):
            raise ValueError("FAQ data must be a JSON list")
        return faqs

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        tokens = text.split()
        tokens = [token for token in tokens if token not in self.stopwords]

        suffixes = ("ies", "ied", "ing", "ed", "es", "s")
        stems = []
        for token in tokens:
            if len(token) > 4:
                for suffix in suffixes:
                    if token.endswith(suffix):
                        token = token[:-len(suffix)]
                        break
            stems.append(token)
        return " ".join(stems)

    def get_response(self, message):
        if not self.faqs or self.faq_matrix is None:
            return self._fallback(0.0)

        processed = self.preprocess(message)
        if not processed:
            return self._fallback(0.0)

        query_vector = self.vectorizer.transform([processed])
        similarities = cosine_similarity(query_vector, self.faq_matrix)[0]
        best_index = int(similarities.argmax())
        confidence = float(similarities[best_index])

        if confidence >= self.confidence_threshold:
            faq = self.faqs[best_index]
            return {
                "reply": faq["answer"],
                "matched_question": faq["question"],
                "confidence": round(confidence, 4),
                "status": "success"
            }
        return self._fallback(confidence)

    def _fallback(self, confidence):
        return {
            "reply": (
                "Sorry, I couldn’t find an answer to that question. Please try "
                "rephrasing it or ask about admissions, courses, fees, "
                "eligibility, or contact details."
            ),
            "matched_question": None,
            "confidence": round(confidence, 4),
            "status": "fallback"
        }
