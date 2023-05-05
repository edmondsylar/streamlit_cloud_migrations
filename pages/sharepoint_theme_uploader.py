import streamlit as st
import os

upload_tab, configs_tab, connect_tab = st.tabs(['Upload Theme','Configurations', 'Connect'])


def execute_ps_script(site_url, username, password):
    # Define the PowerShell script contents
    script = f"""
    $username = "{username}"
    $password = ConvertTo-SecureString "{password}" -AsPlainText -Force
    $cred = New-Object System.Management.Automation.PSCredential($username, $password)
    Connect-SPOService -Url {site_url} -Credential $cred
    """

    # Write the PowerShell script to a temporary file
    with open("temp_script.ps1", "w") as f:
        f.write(script)

    # Execute the PowerShell script
    exec_response = os.system("powershell.exe -ExecutionPolicy Bypass -File temp_script.ps1")
    if exec_response:
        st.write(exec_response)
    else:
        st.write(exec_response)
    # Remove the temporary script file
    # os.remove("temp_script.ps1")


# Add headers to the tabs
with upload_tab:
    st.header("SharePoint Theme Uploader - Upload")
    st.write("Enter the themepalette data and SharePoint site URL:")
    
    # Create the form for themepalette data and site URL
    target_site_url = st.text_input("Target Site URL")
    themepalette_data = st.text_area("Themepalette Data")
    
    # Create a button to submit the form
    if st.button("Upload Theme"):
        # Code to upload the themepalette to SharePoint using PowerShell
        pass


with configs_tab:
    st.header("SharePoint Theme Uploader - Configs")
    st.write("Enter SharePoint authentication information:")
    
    # Create the form for authentication information
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    site_url = st.text_input("Site URL")
    
    # Create a button to submit the form
    if st.button("Submit"):
        # Code to authenticate and connect to SharePoint using PowerShell
        pass


with connect_tab:
    st.header("SharePoint Theme Uploader - Connect")
    st.write("Enter SharePoint connection information:")
    
    # Create the form for connection information
    sp_admin_site_url = st.text_input("Tenant admin Site URL")

    st.markdown("Auth")
    user_name = st.text_input("Username | email")
    pass_word = st.text_input("Auth Password", type="password")
    
    # Create a button to connect to the site
    if st.button("Connect"):
        # Code to connect to SharePoint using PowerShell
        # call the connection function.
        execute_ps_script(sp_admin_site_url, user_name, pass_word)
        pass

