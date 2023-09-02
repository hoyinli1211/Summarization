import streamlit as st
from transformers import pipeline

model_name = "sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization", model=model_name)

st.title("Streamlit Question Answering App")

text_input = st.text_input("Text Input:")
if text_input:
  output = summarizer(text, max_length=130, min_length=30, do_sample=False)
  st.text_area("Result:", output)
