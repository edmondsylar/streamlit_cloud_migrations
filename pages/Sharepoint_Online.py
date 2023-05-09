import streamlit as st
from controllers.auth_2 import SharePointClient
import yaml
from controllers.functions import OfficeConfig
import time
from rich.console import Console

# import sample data from Data/Samples.py
from pages.Data.Samples import sites

console = Console()

st.header("Dashboard")
# configure sharepoint connection.
oConf = OfficeConfig()
# we can have a dashboard here.

st.write('Dashboard Comming here.')

Logs, runs = st.tabs(["Libary Search", "Migrations"])

selected_sp_site = None

# create a variable to store the active selected site.
active_site = None

# function creates the active site
def create_active_site(data):
    pass


# let's experiment with an independent side menu on this one
with st.sidebar:
        st.write("Testing Custom Side Bar")

def create_tabs(list_of_dicts):
    # Create a list of tab titles
    tab_titles = [d['Title'] for d in list_of_dicts]
    # Create a tab for each title
    tabs = st.tabs(tab_titles)
    
    # Iterate over the tabs and add content to each one
    for i, tab in enumerate(tabs):
        with tab:
            Library = list_of_dicts[i]
            st.markdown("## {}".format(Library['Title']))
            
            col1, col2 = st.columns(2)
            with col1:
                # create a form to Enter location of the Data we need to the library.
                with st.form(key='sp_form_migration_{}'.format(i)):
                    # create a text input for the user to enter the location of the data.
                    location = st.text_input("Location")
                    submit = st.form_submit_button(label="Submit")
                    if submit:
                        st.success('You have entered {}'.format(location))

            with col2:
                # create a form to Upload document and folders.
                with st.form(key='sp_form_upload_{}'.format(i)):
                    # create a text input for the user to enter the location of the data.
                    upload = st.file_uploader("Upload Files", accept_multiple_files=True)
                    submit = st.form_submit_button(label="Submit")
                    if submit:
                        console.log(selected_sp_site)
                        # call the upload_to_libary function from OfficeClient
                        if selected_sp_site is not None:
                            upload_process = OfficeClient.upload_to_library(selected_sp_site, Library['Title'], upload)
                            st.success('You have uploaded {}'.format(upload))
                        else:
                            st.warning({
                                "Smg":"Something went Wrong!",
                                "selected_sp_site": selected_sp_site,
                                "Response": upload_process, 
                                })
                



def selectable_tabs(list_of_dicts):
    # Create a list of tab titles
    tab_titles = [d['Title'] for d in list_of_dicts]
    
    # Create a radio button for each tab title
    selected_tab = st.radio('Select a tab', tab_titles)
    
    # Display the contents of the selected tab
    for d in list_of_dicts:
        if d['Title'] == selected_tab:
            st.write(d)

def entry():
    with Logs:
        libs = None
        with st.form(key='sp_form_search'):
            sp_site = st.text_input("Sharepoint site url")
            # sp_library = st.text_input("Sharepoint Library")
            submit = st.form_submit_button(label="Search")
            if submit:
                try:
                    libs = OfficeClient.get_libraries(sp_site)
                    selected_sp_site = sp_site
                except Exception as ex:
                    st.write(ex)

        if libs is not None:
            st.markdown("## Sharepoint Libraries:")
            create_active_site(libs)
            create_tabs(libs)


# decalre the office client
try:
    OfficeClient = SharePointClient(oConf['env_url'], oConf['username'], oConf['password'])
    entry()
except Exception as error:
    st.markdown("""
    ## Authentication   
    This feature requires authenticating with Microsoft 365   
    in order to enable this feature, you will need to login with your   
    office365 account to access the sharepoint environment.

    ### Error Encountered
    {}
    """.format(error))