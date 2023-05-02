import streamlit as st
import yaml
import os

st.header("Configurations")
# st.divider()

tab_1, tab_2, tab_3 = st.tabs(["Current Configuration", "Edit Configuration", "Office Configuration"])

def office_config():
    # Create a form to collect the configuration values
    with st.form(key='config_form'):
        env_url = st.text_input('Enter the env_url')
        site_url = st.text_input('Enter the site_url')
        username = st.text_input('Enter the username')
        password = st.text_input('Enter the password', type='password')
        submit_button = st.form_submit_button(label='Save Configuration')
    
    # Check if the form was submitted
    if submit_button:
        # Create a dictionary with the configuration values
        config = {
            'env_url': env_url,
            'site_url': site_url,
            'username': username,
            'password': password
        }
        
        # Write the configuration to the config.yaml file
        with open('office_config.yaml', 'w') as file:
            yaml.dump(config, file)
            st.success("New Office Configuration Loaded")


with tab_1:
    st.subheader('Running Config')

    if os.path.exists("config.yaml"):
        # Load the configuration from the YAML file
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)

            if config:
                # Display the current configuration
                st.write(f"SharePoint Site URL: {config['site_url']}")
                st.write(f"Username: {config['username']}")
                st.write(f"Password: {'*' * len(config['password'])}")
            else:
                st.warning("There seems to be no running configuration yet")
    else:
        st.title("System Configuration")
        st.warning("You have no configuration loaded yet!")

with tab_2:
    st.subheader('Create | Edit Configuration')
    # Create a form on the Configurations page
    with st.form(key='office_config_form'):
        # Collect SharePoint site information from the user
        site_url = st.text_input('SharePoint Site URL')
        username = st.text_input('Username')
        password = st.text_input('Password')

        # Create a submit button for the form
        submit_button = st.form_submit_button(label='Save Configuration')

        # Save the configuration to a YAML file when the form is submitted
        if submit_button:
            config = {'site_url': site_url, 'username': username, 'password': password}
            with open('config.yaml', 'w') as f:
                yaml.dump(config, f)
                st.success("New Configuration Loaded")

with tab_3:
    st.subheader("Office Configurations")
    office_config()