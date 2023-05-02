import os 
import streamlit as st 
from controllers.sync_upload import Migrator

migrator = Migrator("HFB_migrations.db")
# out app init Function.
def __init_app():
    # initialize application data and state.
    pass

def render_workspace():
    # check database connectivity
    if migrator.conn is None:
        # Display the database status using the st.metric component
        st.metric(label='DB Status', value='Down', delta_color='inverse')
    else:
        # Query the number of records in the migrations table
        migrator.cursor.execute('SELECT COUNT(*) FROM migrations')
        record_count = migrator.cursor.fetchone()[0]

        # Display the database status and record count using the st.metric component
        st.metric(label='DB Status', value=f'{record_count} records', delta='Up', delta_color='normal')
    st.title("Migration Dashboard")
    # st.divider()

    # Migration Instructions
    instructions = """
    ## Migration Instructions

    #### Entering the Directory Paths
    - On the **Workspace** page, locate the input fields for the local directory path and the remote SharePoint directory path.
    - Enter the local directory path (mapped as a network drive) in the appropriate input field.
    - Enter the remote SharePoint directory path in the appropriate input field.

    #### Starting the Migration
    - Click on the **Migrate** button to start migrating files from the local directory to the remote SharePoint directory.
    - Wait for the migration process to complete. You can view the progress of the migration on the **Workspace** page.
    - Once the migration is complete, you will see a confirmation message on the **Workspace** page.
    """

    #set 2 columns
    new_migrations_tab, running_migrations = st.tabs(['New Migration', 'Running Migration'])

    with new_migrations_tab:
        st.header("Migrate")
        with st.form(key='migration_form'):
        # Create two columns for the input fields
            col_1, col2 = st.columns(2)

            # Create input fields for the local and remote directory paths
            local_path = col_1.text_input('Local directory path')
            remote_path = col2.text_input('Remote SharePoint directory path')

            # Create a submit button for the form
            submit_button = st.form_submit_button(label='Migrate')

        # Handle form submission
            if submit_button:
                # call the migrtor function
                _resp = migrator.migrate_files(local_path, remote_path)
                st.write(_resp)


        st.markdown(instructions)


    with running_migrations:
        st.header("Running Migrations")


def _initial_config():
    # Check if the configuration file exists
    if os.path.exists('config.yaml'):
        # Call the render_workspace function
        render_workspace()
    else:
        # Display a warning message and a button to redirect the user to the Configurations page
        st.title("System Configuration")
        st.warning("You have no configuration loaded yet!")
        if st.button('Go to Configurations'):
            # Redirect the user to the Configurations page
            st.experimental_set_page_config(page_title='Configurations') # type: ignore

_initial_config()