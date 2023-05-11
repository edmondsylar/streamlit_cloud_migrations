# streamlit page for testing the Office365_api in Controllers/Office365_api.
import streamlit as st #type:ignore 
from controllers.Office365_api import SharePoint
from rich.console import Console #type:ignore 

# define the console object
console = Console()

# create an instance of SharePoint class
sp = SharePoint(
    "https://housingfinancecoug.sharepoint.com/",
    "SpAdmin@housingfinance.co.ug",
    "#p@ssw0rd123",
    "Shared Documents/"
)

# console log the sharepoint object.
console.log("Lastest Log", SharePoint)

# Page title in markdown
st.markdown("## Office365 API Tests")

# create 2 tabs in the app
tab1, tab2 = st.tabs(["Migrations", "Tests"])

with tab1:
    # simple form to take input
    with st.form("my_form"):
        folder = st.text_input("Library Name:")
        submit = st.form_submit_button("Submit")

        if submit:
            # call the get files list method
            files_list = sp._get_files_list(folder)
            # log the files list
            console.log(files_list)
            # write this to the screen
            st.write(files_list)





