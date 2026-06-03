# 🎥 AI Summarizer Backend

A FastAPI-powered backend application that generates AI-driven summaries from YouTube videos. The system extracts transcripts, processes content using Large Language Models (LLMs), and returns concise, meaningful summaries through REST APIs.

---

## 🚀 Features

* 🎥 YouTube Video Transcript Extraction
* 🤖 AI-Powered Content Summarization
* 📝 Concise and Structured Summaries
* ⚡ FastAPI REST API
* 🔗 Frontend Integration Support
* 📄 PDF Summary Generation Support
* 🏗️ Modular Project Architecture
* 🔄 Easy Deployment and Scalability

---

## 🛠️ Tech Stack

### Backend Framework

* FastAPI
* Uvicorn

### AI & NLP

* LangChain
* OpenAI / Gemini
* Prompt Engineering

### Utilities

* Python
* Requests
* YouTube Transcript API

### Document Generation

* ReportLab

---

## 📂 Project Structure

```text
AI-Summarizer-Backend/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── prompts/
│   ├── summary_prompt.py
│   └── ...
│
├── utils/
│   ├── get_transcript.py
│   ├── generate_summary.py
│   ├── pdf_generator.py
│   └── ...
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Summarizer-Backend.git
```

### 2. Navigate to Project

```bash
cd AI-Summarizer-Backend
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_api_key
```

or

```env
GEMINI_API_KEY=your_api_key
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 📡 API Workflow

```text
User Provides YouTube URL
            │
            ▼
Extract Transcript
            │
            ▼
Process with AI Model
            │
            ▼
Generate Summary
            │
            ▼
Return Response
```

---

## 🎯 Use Cases

* Educational Video Summarization
* Podcast Summaries
* Lecture Notes Generation
* Meeting Recording Summaries
* Content Research Assistance
* Quick Video Insights

---

## 🔮 Future Enhancements

* Multi-Language Summaries
* Speaker Identification
* Chat with Video Feature
* Advanced PDF Reports
* Voice Summaries
* RAG-based Knowledge Retrieval
* User Authentication & History

---

## 👨‍💻 Author

**Ahmar Amjad**

Generative AI Developer | AI Engineer

Passionate about building AI-powered applications using LLMs, FastAPI, LangChain, and Agentic AI systems.

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
