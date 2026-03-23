# 🧠 Named Entity Recognition (NER) using NLP

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NLP](https://img.shields.io/badge/NLP-Named%20Entity%20Recognition-orange)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-LSTM-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

This project implements a **Named Entity Recognition (NER)** system using **Natural Language Processing (NLP)** techniques to identify and classify entities in text into predefined categories such as:

- Person
- Organization
- Location
- Date
- Miscellaneous entities

NER is widely used in applications like **information extraction, chatbots, search engines, and document analysis systems.**

---

# 🚀 Project Overview

Understanding unstructured text is a major challenge in real-world applications.  
This project builds a **machine learning-based NER system** that can automatically extract meaningful entities from raw text data.

The system helps in:

- Extracting structured information from text
- Automating document analysis
- Enhancing search and recommendation systems

---

# 📊 Dataset

The dataset consists of:

- Sentences (text data)
- Corresponding entity tags (labels)

Each word in a sentence is tagged using standard NER tagging formats such as:

- **B-** → Beginning of an entity  
- **I-** → Inside of an entity  
- **O** → Outside any entity  

---

# 🧠 Machine Learning Workflow

The project follows a structured **NLP pipeline**.

## 1️⃣ Data Preprocessing

- Tokenization of sentences
- Handling missing values
- Converting words and tags into numerical format
- Padding sequences for uniform input length

---

## 2️⃣ Feature Engineering

- Word indexing
- Label encoding for entity tags
- Sequence preparation for model training

---

## 3️⃣ Model Building

Implemented a **Deep Learning model (LSTM-based architecture)** for sequence labeling.

### Model Components:

- Embedding Layer
- LSTM Layer
- Dense Layer with Softmax activation

The model learns contextual relationships between words to accurately identify entities.

---

## 4️⃣ Model Training

- Trained on labeled sequence data
- Optimized using appropriate loss function and optimizer
- Evaluated on validation dataset

---

## 5️⃣ Model Evaluation

Evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

These metrics ensure the model performs well on **sequence prediction tasks**.

---

# 📈 Example Output

Input Sentence:


Barack Obama visited India in 2015


Predicted Entities:

- Barack Obama → Person  
- India → Location  
- 2015 → Date  

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- TensorFlow / Keras
- Scikit-learn
- Natural Language Processing (NLP)

---

# 📂 Project Structure


named-entity-recognition/
│
├── named-entity-recognition.ipynb
│ Complete NLP workflow and model training
│
├── model.h5
│ Trained deep learning model
│
├── requirements.txt
│ Project dependencies
│
└── README.md
│ Project documentation


---

# ⚙️ Installation

Clone the repository:


git clone [https://github.com/yourusername/named-entity-recognition.git](https://github.com/Vandanasharma-1/NER)

cd named-entity-recognition


Install dependencies:


pip install -r requirements.txt


---

# ▶️ Run the Project

Open the Jupyter Notebook:


jupyter notebook named-entity-recognition.ipynb


---

# 📈 Business Impact

Named Entity Recognition systems are widely used in:

✔ Chatbots and virtual assistants  
✔ Resume parsing systems  
✔ Information extraction from documents  
✔ Search engines and recommendation systems  

This project demonstrates how **NLP and deep learning can transform unstructured text into actionable insights.**

---

# 👩‍💻 Author

**Vandana Sharma**

Data Scientist | Machine Learning | AI Enthusiast

Passionate about building **AI-powered NLP systems, deep learning models, and real-world data-driven solutions.**

---

⭐ If you found this project useful, consider giving it a **star**!
