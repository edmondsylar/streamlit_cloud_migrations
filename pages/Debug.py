import streamlit as st
from controllers.auth_2 import SharePointClient
import yaml
from controllers.functions import OfficeConfig

# still useless right now
def Logger(header,data):
    st.header(header)
    st.markdown("""
    ## Loging Info.   
    {}
    """.format(data))

st.header("Debug Logs and runs")
# configure sharepoint connection.
oConf = OfficeConfig()
st.write(oConf)

Logs, runs = st.tabs(["Libary Search", "Migrations"])

def create_tabs(list_of_dicts):
    # Create a list of tab titles
    tab_titles = [d['Title'] for d in list_of_dicts]
    
    # Create a tab for each title
    tabs = st.tabs(tab_titles)
    
    # Iterate over the tabs and add content to each one
    for i, tab in enumerate(tabs):
        with tab:
            # Display the contents of the corresponding dictionary
            st.write(list_of_dicts[i])

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

        st.write("Sharepoint Library | Tests")
        with st.form(key='sp_form_search'):
            sp_site = st.text_input("Sharepoint site")
            # sp_library = st.text_input("Sharepoint Library")
            submit = st.form_submit_button(label="Search")

            if submit:
                try:
                    libs = OfficeClient.get_libraries(sp_site)
                except Exception as ex:
                    st.write(ex)

        st.markdown("## SP Libraries")
        if libs is not None:
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
    """)
# check that there is a valid connection.



    

