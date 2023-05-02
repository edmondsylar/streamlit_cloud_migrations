import streamlit as st
import yaml
import os

st.header("Configurations")
# st.divider()

tab_1, tab_2 = st.tabs(["Current Configuration", "Edit Configuration"])

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
    # Create a form on the Configurations page
    with st.form(key='config_form'):
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