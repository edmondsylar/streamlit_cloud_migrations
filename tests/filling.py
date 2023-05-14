import os

def read_directory(directory_location):
    for filename in os.listdir(r"{}".format(directory_location)):
        with open(os.path.join(directory_location, filename)) as file:
            print(file.read())

# get current directory
current_directory = os.getcwd()

# navigate to the tests folder inside the current directory
os.chdir(r"{}".format(current_directory))


read_directory('/home/edmondsylar-ubuntu/development/streamlit_cloud_migrations/tests')