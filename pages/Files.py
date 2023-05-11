from dotenv import load_dotenv #type:ignore
import streamlit as st #type:ignore
from PyPDF2 import PdfReader #type:ignore
from langchain.text_splitter import CharacterTextSplitter #type:ignore
import hfapi #type:ignore

client = hfapi.Client("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")

notification = st.empty()
def update_notification(data):
   notification.write(data)
def how_to():
    st.subheader("Wanna get this Working!") 

def configurations():
    st.subheader("Openai configurations") 


def main():
    st.subheader("Ask your Files 💬")
    col1, col2 = st.columns([0.35, 0.65])

    context = ""
    load_dotenv()        
    # upload file
    with col1:
     
      pdf = st.file_uploader("Upload your PDF", type="pdf")
      
      notification.write("")

      # extract the text
      if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
          text += page.extract_text()
          
        # split into chunks
        text_splitter = CharacterTextSplitter(
          separator="\n",
          chunk_size=1000,
          chunk_overlap=200,
          length_function=len
        ) # type: ignore
        chunks = text_splitter.split_text(text)
        
        # add the chucks to the context
        context += "\n".join(chunks)
        update_notification("Loading Document Context Completed")

      with col2:
        st.markdown("### Ask a question")
        with st.form(key="query_form"):
          user_question = st.text_input("Ask a question about your PDF:")
          submit = st.form_submit_button("Submit")
          if submit:
            # get response from the context
            response = client.question_answering(user_question, context)
            print(response)
            st.success(response)

      # show user input
      
    


# 
st.header("Qurey FIles.")

home, _howTo, config = st.tabs(['Home', 'How to', 'Configurations'])

with home:
  main()


with _howTo:
  how_to()

with config:
   configurations()