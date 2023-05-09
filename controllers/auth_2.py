from shareplum import Site
from shareplum import Office365
import os

class SharePointClient:
    def __init__(self, env_url, username, password):
        # Authenticate with SharePoint using Office 365 authentication
        self.authcookie = Office365(env_url, username=username, password=password).GetCookies()
    
    def format_folder_path(self, folder_path):
        return folder_path.replace('\\', '\\\\') # type: ignore
    
    def get_documents(self, site_url, doc_library_name):
        self.site = Site(site_url, authcookie=self.authcookie)
        # Get the document library
        sp_list = self.site.List(doc_library_name) # type:ignore
        
        # Get all items from the list
        data = sp_list.GetListItems()
        print(data)
        # Return the data
        return data
    
    def upload_files(self, site_url, doc_library_name, folder_path):
        self.site = Site(site_url, authcookie=self.authcookie)
        # Get the document library
        sp_list = self.site.List(doc_library_name) # type:ignore
        
        # Upload all files in the directory
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'rb') as file:
                sp_list.UpdateListItems(data=file.read(), kind='New', filename=file_name) # type:ignore

        # check the files that have uploaded.
        uploads = self.get_documents(site_url, doc_library_name)
        print(uploads)

    def get_libraries(self, site_url):
        self.site = Site(site_url, authcookie=self.authcookie)
        # Get all lists and libraries on the site
        lists = self.site.GetListCollection() # type:ignore
        
        # Filter the results to only include document libraries
        libraries = [l for l in lists if l['BaseType'] == 'DocumentLibrary'] # type:ignore
        
        # Return the list of document libraries
        return libraries

