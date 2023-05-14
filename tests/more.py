from office365.runtime.auth.client_credential import ClientCredential #type:ignore
from office365.sharepoint.client_context import ClientContext #type:ignore
import uuid
import tempfile
import os

m365_client_ID = "b00013bf-c9fe-4e0f-9d87-0ba758476640" # Application ID
m365_secret = "979adc70-a759-4093-80d9-afc34fc907dc"


def upload_file(content, document_library):
    # Get sharepoint credentials
    sharepoint_url = 'https://housingfinancecoug.sharepoint.com/'
    client_credentials = ClientCredential(m365_client_ID, m365_secret)

    # Create client context object
    ctx = ClientContext(sharepoint_url).with_credentials(client_credentials)

    # Get the document library by its name
    library = ctx.web.lists.get_by_title(document_library)

    # Get the root folder of the document library
    root_folder = library.root_folder

    # Load and execute the query
    ctx.load(root_folder)
    ctx.execute_query()

    # Generate a random file name
    file_name = str(uuid.uuid4()) + ".txt"

    # Create a temporary file path
    file_path = os.path.join(tempfile.gettempdir(), file_name)

    # Write the content to the temporary file
    with open(file_path, "wb") as f:
        f.write(content)

    # Upload the file to the root folder using create_upload_session method
    response = root_folder.files.create_upload_session(
        source_path=file_path,
        chunk_size=1024 * 1024,
    ).execute_query()

    # Remove the temporary file
    os.remove(file_path)

    return response


import requests
from requests_ntlm import HttpNtlmAuth

# Get sharepoint credentials


def option_2(content, document_library, site):
    # Create an NTLM authentication object
    auth = HttpNtlmAuth(username, password)

    # Get the site URL by concatenating the SHAREPOINT_SITE and the site name
    site_url = f"{sharepoint_url}/sites/{site}"

    # Get the document library by its name
    library = web.lists.get_by_title(document_library)

    # Get the root folder of the document library
    root_folder = library.root_folder

    # Load and execute the query
    conn.load(root_folder)
    conn.execute_query()

    # Generate a random file name
    file_name = str(uuid.uuid4()) + ".txt"

    # Create a temporary file path
    file_path = os.path.join(tempfile.gettempdir(), file_name)

    # Write the content to the temporary file
    with open(file_path, "wb") as f:
        f.write(content)

    # Construct the upload URL by appending the file name to the root folder URL
    upload_url = root_folder.properties["ServerRelativeUrl"] + "/" + file_name

    # Upload the file using requests.put method with auth and headers
    headers = {"accept": "application/json;odata=verbose"}
    response = requests.put(upload_url, data=content, auth=auth, headers=headers)

    # Remove the temporary file
    os.remove(file_path)

    return response


# call the upload_file function
upload_file(r'/home/edmondsylar-ubuntu/Downloads/cmake-3.26.3-linux-x86_64.sh', 'Local_migration_test')