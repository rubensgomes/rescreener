## NLP (Natural Language Processing)

### 🧠 What is NLP?

Natural Language Processing is a branch of AI that focuses on enabling computers
to understand, interpret, and generate human language — whether it's written (
text) or spoken.

### Use of NLP on This Project

🧾 In the Resume Screener Project (`rescreener`):

You're dealing with unstructured text data — like:

- Candidate resumes (PDFs or raw text)

- Job descriptions (text with skills, roles, requirements)

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

### Example NLP Techniques Used in Projects

| Task                           | NLP Technique                                |
|--------------------------------|----------------------------------------------|
| Clean and parse text           | Tokenization, stopword removal               |
| Analyze meaning                | Word embeddings, BERT, GPT                   |
| Text classification            | Logistic regression, fine-tuned transformers |
| Text similarity                | Cosine similarity on embeddings              |
| Generate summaries or feedback | LLMs like GPT or Claude                      |

## Use of NLP in Other Projects

💡 In other projects (like product recommender), NLP is used to:

- Understand product descriptions

- Cluster or group similar products

- Create natural-language interfaces (e.g., "Show me vegan-friendly jackets
  under $100")