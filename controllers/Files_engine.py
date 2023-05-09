import streamlit as st 
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import tensorflow_hub as hub
import numpy as np



def create_embeddings(data):
    st.write(data)
    # load pre-trained model for sentence embeddings
    model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model = hub.load(model_url)

    # create embeddings for sentences
    embeddings = model(data)

    # convert embeddings to numpy array
    embeddings = np.array(embeddings)

    return embeddings


# this function is going to use PdfReader to read the pdf file
def read_doc(pdf_file):
    text = ""
    for page in PdfReader(pdf_file).pages:
        text += page.extract_text()
    return text

def main():
    consolidate_data = ""
    # Set page title
    st.set_page_config(page_title='Document Search Engine', 
                       page_icon=':mag:', 
                       layout='wide')

    # Define sidebar
    st.sidebar.title('Upload PDF File')
    uploaded_files = st.sidebar.file_uploader('Choose files', accept_multiple_files=True)
    # Define main content
    st.title('Document Search Engine')
    if consolidate_data == "":
        st.write('Upload some files to get started!')


    if uploaded_files:
        for each_file in uploaded_files:
            _extract = read_doc(each_file)
            # after we have the response we will consolidate the data
            consolidate_data += _extract
        
        # we are noe going to split the consolidate data into chunks
        _chunks = text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        embeddings = create_embeddings(consolidate_data) # type:ignore
        # Knowledge_base = FAISS.from_texts(_chunks, embeddings)  # type: ignore
        st.write(embeddings)





if __name__ == '__main__':
    main()


