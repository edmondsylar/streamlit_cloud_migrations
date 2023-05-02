from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

def get_documents(site_url, username, password):
    # Authenticate with SharePoint
    authcookie = Office365(site_url, username=username, password=password).GetCookies()
    site = Site(site_url, version=Version.v2016, authcookie=authcookie)
    
    # Get the 'Documents' list
    sp_list = site.List('Documents') # type:ignore
    
    # Get all items from the list
    data = sp_list.GetListItems()
    
    # Return the data
    return data