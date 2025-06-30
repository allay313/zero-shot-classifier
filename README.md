# 🧠 Zero-Shot Text Classifier with Gradio

Classify your text into the most relevant category — even if the model has never seen those labels before! Built using Hugging Face Transformers and Gradio.

---

## 🔍 About the Model
- **Pipeline:** `zero-shot-classification`
- **Model:** `facebook/bart-large-mnli`
- **Framework:** Hugging Face Transformers
- **Task:** Predicts the best-matching label from your custom list

---

## 💡 Features
- Real-time zero-shot classification
- Input any sentence and custom labels
- Displays label ranking with confidence percentages
- Beginner-friendly, deployed via Hugging Face Spaces

---

## 📌 Instructions for Users
This app uses **zero-shot learning** to match your input with the most appropriate label from your list — without prior training on those labels.

👉 **How to use:**
1. Enter a sentence or paragraph
2. Provide comma-separated labels like: `Technology, Sports, Food`
3. View ranked predictions with confidence scores

⚠️ **Note:**
- Overlapping or vague labels may affect accuracy
- For example, a sentence about healthcare policy may score both **Health** and **Finance**

✅ **Example:**
- **Text:** `Apple just launched the new iPhone with advanced camera features and longer battery life.`
- **Labels:** `Technology, Food, Sports`
- **Prediction:** `Technology — 96.8%`

---

## 🚀 Live Demo
👉 Try it here: [Zero-Shot Text Classifier on Hugging Face Spaces](https://huggingface.co/spaces/PaulSouvik/zero-shot-classifier)

---

## 📦 Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the app locally:
```bash
python app.py
```

---

## 📄 License
Apache-2.0
