# CodeAlpha FAQ Chatbot

A responsive AI FAQ chatbot built for the CodeAlpha AI Internship Task 3. It matches natural-language questions with a curated FAQ dataset using TF-IDF and cosine similarity.

## Features

- Clean, responsive desktop and mobile chat interface
- TF-IDF vectorization and cosine-similarity matching
- 18-domain FAQ entries covering courses, admissions, fees, eligibility, certificates, refunds, support, and more
- Configurable `0.35` confidence threshold
- Quick reply buttons
- Typing indicator, Clear Chat, empty-input prevention, and network error handling
- JSON REST API

## Technologies

- Python 3
- Flask
- scikit-learn
- HTML, CSS, and JavaScript
- JSON

## Project Structure

```text
CodeAlpha_FAQ_Chatbot/
├── static/
│   ├── css/style.css
│   └── js/script.js
├── templates/index.html
├── data/faqs.json
├── app.py
├── chatbot.py
├── requirements.txt
├── spec.md
├── README.md
└── .gitignore
```

## Installation

1. Open a terminal in the project folder.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## API

### Chat endpoint

`POST /api/chat`

Request:

```json
{
  "message": "What courses are available?"
}
```

Successful response:

```json
{
  "reply": "We offer Artificial Intelligence, Web Development, Data Science, and Python Programming courses.",
  "matched_question": "What courses do you offer?",
  "confidence": 0.87,
  "status": "success"
}
```

Fallback response:

```json
{
  "reply": "Sorry, I couldn’t find an answer to that question. Please try rephrasing it.",
  "matched_question": null,
  "confidence": 0.21,
  "status": "fallback"
}
```

## Adding FAQs

Edit `data/faqs.json`. Give each entry a unique `id`, a natural-language `question`, an accurate `answer`, relevant `keywords`, and a `category`. Restart the Flask server after changing the dataset.

## Screenshots

Place screenshots in `static/images/` and add them here after testing:

- Desktop chat interface
- Mobile chat interface
- Successful FAQ response
- Fallback response

## Future Improvements

- Voice input and text-to-speech
- Multi-language support
- Admin FAQ editor
- Database-backed FAQ storage and chat history
- Optional LLM-assisted suggestions
- Helpful/Not Helpful feedback and analytics

## Repository

Repository name: `CodeAlpha_FAQ_Chatbot`

Created as part of the **CodeAlpha AI Internship**. This project is independently built for learning and portfolio purposes.
