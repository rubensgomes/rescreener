# rescreener

AI-Powered Resume Screener (Classification + NLP + LLM)

- NLP stands for Natural Language Processing

Problem: Automatically classify or rank resumes based on job description fit.

Stack:
Data: Sample resumes + job descriptions (or scrape)

ML: Embedding with BERT + classifier (e.g., logistic regression or fine-tuned
transformer)

Backend: FastAPI to score resumes

Frontend: Upload interface + match score

Bonus: Use OpenAI or Hugging Face LLM to generate feedback comments

## NLP (Natural Language Processing)

NLP is used to:

- Extract and clean text from resumes and job descriptions
- Convert words into numerical representations (called embeddings) using methods
  like:
    - TF-IDF
    - Word2Vec / GloVe
    - Transformer-based models like BERT
- Compare similarity between a resume and a job description
- Classify resumes based on their fit (e.g., "Good match", "Maybe", "Not a fit")
- Optionally: Generate interview questions or feedback using LLMs (a form of
  generative NLP)

## Example NLP Techniques Used in Projects

| Task              	             | NLP Technique                                |
|---------------------------------|----------------------------------------------|
| Clean and parse text	           | Tokenization, stopword removal               |
| Analyze meaning	                | Word embeddings, BERT, GPT                   |
| Text classification	            | Logistic regression, fine-tuned transformers |
| Text similarity	                | Cosine similarity on embeddings              |
| Generate summaries or feedback	 | LLMs like GPT or Claude                      |

## Input Dataset

In this project we're dealing with unstructured text data — like:

- Candidate resumes (PDFs or raw text)
- Job descriptions (text with skills, roles, requirements)

## ChapGPT

**NOTE:** This project was created with the help
of [ChapGPT](https://chatgpt.com/)


---
[Rubens Gomes](https://rubensgomes.com)