# CodeAlpha FAQ Chatbot Specification

## Domain
CodeAlpha internship, courses, admissions, and student support.

## Matching configuration
- Minimum cosine-similarity confidence: `0.35`
- Text preprocessing: lowercase, punctuation removal, stopword filtering, lightweight stemming
- Vectorization: TF-IDF with unigrams and bigrams
- Matching: cosine similarity

## API
- `POST /api/chat`
- Request: `{ "message": "..." }`
- Success: answer, matched FAQ, confidence, and success status
- Fallback: fallback answer, null matched FAQ, confidence, and fallback status
- Invalid input and server errors return appropriate JSON error responses

## UI
Responsive desktop/mobile chat interface with quick replies, typing indicator, clear chat, send disabling, and network error handling.
