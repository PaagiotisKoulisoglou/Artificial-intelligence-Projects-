# 🧠 Wikipedia RAG AI Assistant

This is a simple, educational app built with Streamlit that uses **RAG (Retrieval-Augmented Generation)** to answer questions about AI and machine learning using content from **Wikipedia**.

It combines OpenAI’s language models with Wikipedia articles to give accurate answers and show exactly where the info came from.

---

## 🚀 What It Does

- Downloads and indexes selected Wikipedia pages (e.g. Neural Networks, Deep Learning, etc.)
- Uses OpenAI's embedding model to create a searchable vector index
- Lets you ask questions in natural language
- Responds with a clear answer + the actual Wikipedia text used

---

## 📦 How to Run It

1. **Clone the repo**   
git clone https://github.com/your-username/wiki-rag-app.git
cd wiki-rag-app

2.Install requirments.txt
 pip install -r requirements.txt

3.Add your OpenAI key
OPENAI_API_KEY=your_api_key_here

4.Start the app
streamlit run app.py
