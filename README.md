# Gemini PDF QA System 

A **Retrieval Augmented Generation (RAG) based Question Answering System** that allows users to ask questions from PDF documents using **Google Gemini, LlamaIndex, and Streamlit**.

This project extracts information from PDFs, creates vector embeddings, and uses **Gemini LLM** to generate accurate answers.

---

#  Features

*  Ask questions from PDF documents
*  Fast semantic search using vector embeddings
*  Powered by Google Gemini LLM
*  Context-aware answers (RAG architecture)
*  Interactive UI using Streamlit
* Persistent vector storage
* Logging and custom exception handling

---

#  Tech Stack

* **LLM:** Google Gemini (gemini-2.5-flash)
* **Framework:** LlamaIndex
* **Embeddings:** Gemini Embedding Model
* **Frontend:** Streamlit
* **Language:** Python
* **Vector Store:** LlamaIndex Storage
* **Environment:** Python, VS Code


# ⚙️ Installation

## Step 1: Clone the repository

```bash
git clone https://github.com/satyam-1605/gemini-pdf-qa-system.git
cd gemini-pdf-qa-system
```

---

## Step 2: Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Add API Key

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

#  Run the Application

```bash
streamlit run streamlitApp.py
```

---

#  How it works

1. Load PDF documents
2. Split text into chunks
3. Generate embeddings
4. Store in vector database
5. User asks question
6. Relevant chunks retrieved
7. Gemini generates answer

---

#  Example

**Question:**

> What is Machine Learning?

**Answer:**

> Machine Learning is a branch of AI that enables systems to learn from data.

---

#  Environment Variables

Required:

```
GOOGLE_API_KEY
```

---

#  Future Improvements

* Chat history memory
* Multi-PDF support
* Deploy on cloud
* Add authentication
* Use advanced vector databases

---

#  Use Cases

* Student study assistant
* Research paper analysis
* Document chatbot
* Knowledge base assistant

---

#  Author

Satyam Chaturvedi

---

#  If you like this project

Please star the repository 
