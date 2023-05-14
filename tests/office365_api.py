import environ #type:ignore
from office365.sharepoint.client_context import ClientContext #type:ignore
from office365.sharepoint.files.file import File #type:ignore
from office365.runtime.auth.user_credential import UserCredential #type:ignore
from time import sleep
import os
import uuid
import tempfile


env = environ.Env()
environ.Env.read_env()

# username = env('sharepoint_email')
# password = env('sharepoint_password')
# sharepoint_site = env('sharepoint_site_url')
# sharepoint_site_name = env('sharepoint_site_name')
# sharepoint_doc = env('sharepoint_doc_library')


class SharePoint:
    def __init__(self):
        self._class_auth = self._auth()

    def _auth(self):
        conn = ClientContext(sharepoint_site).with_credentials(
            UserCredential(username, password)
        )

        return conn
    
    def _get_file_list(self, folder_name):
        conn = self._auth()
        
        print(conn)
        # sleep(0.5)
        sleep(0.5)

        target_folder_url = f'{sharepoint_doc}/{folder_name}'
        root_folder = conn.web.get_folder_by_server_relative_url(target_folder_url)
        
        print(root_folder)
        # sleep(0.5)
        sleep(0.5)

        root_folder.expand(["Files", "Folders"]).get().execute_query()

        return root_folder.files
    
    def download_file(self, file_name, folder_name):
        conn = self._auth()
        file_url = f'/sites/{sharepoint_site}/{sharepoint_doc}/{folder_name}/{file_name}'
        file = File.open_binary(conn, file_url)
        return file.conten
    
    
    def get_folder_list(self, site, document_library):
        conn = self._auth()
        site_url = f"{sharepoint_site}/sites/{site}"

        # declare the web object
        web = conn.web
        library = web.lists.get_by_title(document_library)

        # Get the root folder of the document library
        root_folder = library.root_folder
        root_folder.expand(["Folders"])

        # Load and execute the query
        conn.load(root_folder)
        conn.execute_query()

        # Get the subfolders as a list
        folders = root_folder.folders
        folder_names = []

        for folder in folders:
            folder_names.append(folder.properties["Name"])

        return folder_names
    
    def get_all_files(self, site, document_library):
        # Get a client context object using the _auth method
        conn = self._auth()

        # Get the site URL by concatenating the SHAREPOINT_SITE and the site name
        site_url = f"{sharepoint_site}/sites/{site}"

        # Get the web object for the site
        web = conn.web

        # Get the document library by its name
        library = web.lists.get_by_title(document_library)

        # Get the root folder of the document library
        root_folder = library.root_folder

        # Expand the subfolders and files properties of the root folder
        root_folder.expand(["Folders", "Files"])

        # Load and execute the query
        conn.load(root_folder)
        conn.execute_query()

        # Get the subfolders and files as lists
        folders = root_folder.folders
        files = root_folder.files

        # Create an empty list to store the output objects
        output = []

        # Loop through the folders and get their names and files
        for folder in folders:
            # Get the folder name
            folder_name = folder.properties["Name"]

            # Expand the files property of the folder
            folder.expand(["Files"])

            # Load and execute the query
            conn.load(folder)
            conn.execute_query()

            # Get the files as a list
            folder_files = folder.files

            # Create an empty list to store the file names
            file_names = []

            # Loop through the files and append their names to the list
            for file in folder_files:
                file_names.append(file.properties["Name"])

            # Create an object with the folder name and file names
            obj = {
                "Folder": folder_name,
                "Files": file_names
            }

            # Append the object to the output list
            output.append(obj)

        # Loop through the files in the root folder and append their names to a list
        root_file_names = []
        for file in files:
            root_file_names.append(file.properties["Name"])

        # Create an object with the root folder name and file names
        root_obj = {
            "Folder": document_library,
            "Files": root_file_names
        }

        # Append the object to the output list
        output.append(root_obj)
        return output

    def upload_files(self, site, document_library, content):
        # Get a client context object using the _auth method
        conn = self._auth()

        # Get the site URL by concatenating the SHAREPOINT_SITE and the site name
        site_url = f"{sharepoint_site}/sites/{site}"

        # Get the web object for the site
        web = conn.web

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

        # Upload the file to the root folder using create_upload_session method
        response = root_folder.files.create_upload_session(
            source_path=file_path,
            chunk_size=1024 * 1024,
        ).execute_query()

        # Remove the temporary file
        os.remove(file_path)

        return response
    

    
    def _upload_files(self, site, document_library, content):
        # Get a client context object using the _auth method
        conn = self._auth()

        # Get the web object for the site
        web = conn.web

        # Get the document library by its name
        library = web.lists.get_by_title(document_library)

        # Get the root folder of the document library
        root_folder = library.root_folder

        # Loop through each directory or file path in the content parameter
        for path in content:
            if os.path.isdir(path):
                # If the path is a directory, loop through each file in the directory
                for file_name in os.listdir(path):
                    file_path = os.path.join(path, file_name)
                    with open(file_path, 'rb') as f:
                        # Upload the file to the root folder using add method
                        file_creation_info = {
                            'Url': file_name,
                            'Overwrite': True,
                            'ContentStream': f,
                        }
                        root_folder.files.add(file_creation_info)
            else:
                # If the path is a file, upload it to the root folder using add method
                file_name = os.path.basename(path)
                with open(path, 'rb') as f:
                    file_creation_info = {
                        'Url': file_name,
                        'Overwrite': True,
                        'ContentStream': f,
                    }
                    root_folder.files.add(file_creation_info)

        return response


# test the class 
sp = SharePoint()

# get files 
sp.upload_files(sharepoint_site_name, sharepoint_doc, [r'/home/edmondsylar-ubuntu/Downloads'])