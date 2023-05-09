import streamlit as st 
from nomic.gpt4all import GPT4All
    # m = GPT4All()
    # m.open()
    # story = m.prompt('write me a story about a lonely computer')

st.subheader("Generative Pre-Trained Transformer Testing")
# if story:
#     st.write(story)

# streamlit tabs for configuration and Execution.
configs , execution = st.tabs(['Configurations', 'Execution'])

# display the configurations page.
with configs:
    st.subheader("Configurations")


with execution:
    st.subheader("GPT Model Execution")
    # display the execution page.
    # page has a basic input filed to take the user's request/prompt and sigle submbit button.
    # after the submission a spinner is shown as the results from the model are displayed.
    st.write("This is the execution page")
    with st.form(key="GPT"):
        st.write("Please enter your prompt")
        prompt = st.text_input("")
        submit = st.form_submit_button("Submit")