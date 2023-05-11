import streamlit as st #type:ignore
import requests
import aiohttp #type:ignore

# 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

class asHF_API:
    def __init__(self):
        self.App_name = "Hugging Faces"

    async def analyze_image(self, filename):
        API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-101"
        headers = {"Authorization": "Bearer ******************************************"}

        async with aiohttp.ClientSession() as session:
            with open(filename, "rb") as f:
                data = f.read()
            async with session.post(API_URL, headers=headers, data=data) as response:
                return await response.json()


class HF_API:
    def __init__(self):
        self.App_name = "Hagging Faces"

    

    def analyze_image(self, filename):

        API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-101"
        headers = {"Authorization": "Bearer ******************************************"}

        
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

alifie_module_vision = HF_API()

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
        image = ("image_1.jpg")
        submit = st.form_submit_button("Submit")

        if submit:
            # get details about the uploaded imgae now.
            image_details = alifie_module_vision.analyze_image(image)
            st.write(image_details)






