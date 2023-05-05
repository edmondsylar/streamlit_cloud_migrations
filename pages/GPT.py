import streamlit as st 
from nomic.gpt4all import GPT4All
m = GPT4All()
m.open()
story = m.prompt('write me a story about a lonely computer')

st.subheader("Generative Pre-Trained Transformer Testing")
if story:
    st.write(story)