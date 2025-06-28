# rescreener

AI-Powered Resume Screener (Classification + NLP + LLM)

- NLP stands for Natural Language Processing
- LLM stands for Large Language Model

Problem: Automatically classify or rank resumes based on job description fit.

## Project Structure

This project follows the following standard project layout structure:

```text
    app_name
    ├── pyproject.toml
    ├── poetry.lock 
    ├── README.md
    ├── .gitignore
    │
    ├── app_name/
    │   ├── __init.py__
    │   ├── main.py
    │   ├── module_a.py
    │   └── package/
    │       ├── __init.py__
    │       └── module_b.py
    │
    └── tests/
        ├── __init__.py
        ├── test_main.py
        ├── test_module_a.py
        │   └── package/
        │       ├── __init.py__
        │       └── test_module_b.py
```

## Prerequisite Tools

- pipx 1.7.1 or later
- poetry 2.1.3 or later
- pylint 3.3.7 or later
- python3 3.13.0 or later
- pytest 8.3.4 or later
- IDE (e.g., PyCharm)

## Stack:

- Data: Sample resumes + job descriptions (or scrape)

- ML: Embedding with BERT + classifier (e.g., logistic regression or fine-tuned
  transformer)

- Backend: FastAPI to score resumes

- Frontend: Upload interface + match score

- Bonus: Use OpenAI or Hugging Face LLM to generate feedback comments

## 🧩 Project Blueprint: End-to-End ML Flow

Here’s a general pipeline you should follow regardless of the problem domain:

| Step                             | What You Do                                      | Tools to Use                   |
|----------------------------------|--------------------------------------------------|--------------------------------|
| 1. **Define the problem**        | E.g., classification, regression, recommendation | N/A                            |
| 2. **Collect/Clean Data**        | Load, clean, and analyze your dataset            | Pandas, NumPy                  |
| 3. **EDA & Feature Engineering** | Understand and visualize patterns                | Seaborn, Matplotlib            |
| 4. **Train/Test Split**          | Prepare train/validation sets                    | Scikit-learn                   |
| 5. **Build & Train Models**      | Try several models, tune hyperparameters         | Scikit-learn, XGBoost, PyTorch |
| 6. **Evaluate Models**           | Use metrics like accuracy, F1, RMSE, ROC         | Scikit-learn                   |
| 7. **Deploy the Model**          | Create an API to serve predictions               | Flask or FastAPI               |
| 8. **Build UI or App**           | Web app to interact with the model               | Streamlit, React, Dash         |
| 9. **Monitor & Iterate**         | Add logging, test edge cases, improve UX         | MLflow, logging libs           |


## Input Dataset

In this project we're dealing with unstructured text data — like:

- Candidate resumes (PDFs or raw text)
- Job descriptions (text with skills, roles, requirements)

## Setup of Development Environment

Refer to [SETUP.md](./SETUP.md).

## ChapGPT

**NOTE:** This project was created with the help
of [ChapGPT](https://chatgpt.com/)


---
[Rubens Gomes](https://rubensgomes.com)