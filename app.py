import gradio as gr
from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify(text, labels):
    labels = [label.strip() for label in labels.split(",") if label.strip() != ""]
    if not text or not labels:
        return "Please provide both text and at least one label."
    result = classifier(text, labels)
    output = "\n".join([
        f"{label} — {round(score * 100, 2)}%" for label, score in zip(result['labels'], result['scores'])
    ])
    return output

# Instructions + Example
instructions = """
🧠 **Instructions for Users**

This app uses **zero-shot classification** to predict the most likely category from your custom labels — even if it wasn't specifically trained on those labels!

👉 **How to use:**
1. Enter a sentence or paragraph.
2. Provide 2 or more **comma-separated labels** (e.g., Technology, Food, Sports).
3. The model will return ranked labels with confidence scores.

⚠️ **Note:** Overlapping or vague labels may reduce accuracy. For example:
- A sentence about economics and health policy might rank both **Finance** and **Health**.

✅ **Example:**
- **Text:** "Apple just launched the new iPhone with advanced camera features and longer battery life."
- **Labels:** Technology, Food, Sports
- **Prediction:** Technology — 96.8%
"""

# Gradio Interface
demo = gr.Interface(
    fn=classify,
    inputs=[
        gr.Textbox(label="Enter your text", lines=4, placeholder="e.g. Apple just launched the new iPhone with advanced camera features and longer battery life."),
        gr.Textbox(label="Enter comma-separated labels", placeholder="e.g. Technology, Food, Sports")
    ],
    outputs=gr.Textbox(label="Predicted Labels with Confidence"),
    title="Zero-Shot Text Classifier",
    description=instructions,
    theme="default"
)

if __name__ == "__main__":
    demo.launch()
