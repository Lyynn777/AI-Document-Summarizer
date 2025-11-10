# 🧠AI Document Summarizer Web App

An **AI-powered web application** that summarizes lengthy PDF documents into **concise, readable bullet points** using **Natural Language Processing (NLP)** and **Transformer-based models**.  
Built with **Flask**, **Hugging Face Transformers (T5-small)**, and **pdfplumber** for text extraction.

> ⚙️ *Note:* This project focuses on **readability and efficient local execution**, not on achieving state-of-the-art summarization accuracy. It’s designed to demonstrate how lightweight Transformer models can be integrated into a real-world web application.

---

## 🚀 Features

- 📄 **PDF Upload Support:** Upload any text-based PDF for instant summarization.  
- 🧠 **AI-Powered Summaries:** Uses the `t5-small` model for abstractive text summarization.  
- 🔍 **Clean Formatting:** Automatically cleans, filters, and formats the output into neat bullet points.  
- 💬 **Lightweight & Fast:** Runs locally on CPU — no heavy GPU required.  
- 🌐 **Web Interface:** Simple Flask-based UI for easy interaction.  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS (Flask Templates) |
| **Backend** | Flask (Python) |
| **AI Model** | Hugging Face Transformers (`t5-small`) |
| **PDF Processing** | pdfplumber, PyPDF2 |
| **Environment** | Python 3.10+, Virtualenv |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AI-Document-Summarizer.git
cd AI-Document-Summarizer
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Environment

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application

```bash
python app.py
```

---

## 📂 Project Structure

```
AI-Document-Summarizer/
│
├── app.py                # Flask backend
├── summarizer.py         # AI summarization logic
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML frontend
│   ├── index.html
│   └── summary.html
│
└── static/               # CSS styling
    └── css/
        └── style.css
```
---

## ⚠️ Limitations

While this project demonstrates a functional AI summarization pipeline, it has some practical limitations:

- The `t5-small` model provides concise summaries but may miss deeper context.
- Scanned or image-only PDFs are not supported without OCR.
- Works best for English text; multilingual support not yet implemented.
- Long documents are processed in chunks, which can slightly reduce coherence.

---

## 🌐 Future Enhancements

- Add OCR integration for scanned PDFs.
- Support for `.txt` and `.docx` formats.
- Option to choose summary length (short/medium/detailed).
- Integration with Hugging Face APIs for model selection.
- Deploy on Render or Hugging Face Spaces for public access.

---


⭐ **If you like this project, consider giving it a star** ⭐


