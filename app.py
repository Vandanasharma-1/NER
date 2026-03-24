from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load model and preprocessing objects
model = load_model("model.h5")
word2idx = pickle.load(open("word2idx.pkl", "rb"))
tag2idx = pickle.load(open("tag2idx.pkl", "rb"))
idx2tag = {i: w for w, i in tag2idx.items()}

MAX_LEN = 50

# Preprocess input sentence
def preprocess(sentence):
    words = sentence.split()
    sequence = []

    for word in words:
        sequence.append(word2idx.get(word.lower(), 0))

    # Padding
    padded = sequence + [0]*(MAX_LEN - len(sequence))
    return np.array([padded]), words


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form["text"]
    
    X, words = preprocess(data)
    pred = model.predict(X)
    pred = np.argmax(pred, axis=-1)[0]

    tags = [idx2tag.get(p, "O") for p in pred[:len(words)]]

    result = list(zip(words, tags))

    return render_template("index.html", result=result, text=data)


if __name__ == "__main__":
    app.run(debug=True)