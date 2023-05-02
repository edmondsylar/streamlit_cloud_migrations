import os
import sharepy
import sqlite3
import yaml

class Migrator:
    def __init__(self, db_path):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Create the migrations table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                local_path TEXT NOT NULL,
                remote_path TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def migrate_files(self, local_path, remote_path):
    # Load the configuration from the YAML file
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
            site_url = config['site_url']
            username = config['username']
            password = config['password']

        # Connect to SharePoint site
        # s = sharepy.connect(site_url, username, password)

        # List all files in the local directory
        for file_name in os.listdir(local_path):
            # Construct the local file path
            file_path = os.path.join(local_path, file_name)

            # # Upload the file to the remote SharePoint directory
            # with open(file_path, 'rb') as f:
            #     file_contents = f.read()
            #     r = s.post(f"{site_url}/_api/web/GetFolderByServerRelativeUrl('{remote_path}')/Files/add(url='{file_name}',overwrite=false)", file_contents)

            # Store information about the migration in the SQLite database
            self.cursor.execute("INSERT INTO migrations (file_name, local_path, remote_path) VALUES (?, ?, ?)", (file_name, local_path, remote_path))

            try:
                self.conn.commit()
                return {
                        "code" : 200,
                        "msg" : "Migration Started"
                    }
                    
            except Exception as error:
                return {
                        "code" : 500,
                        "msg" : "Something Went wrong",
                        "SystemReturn" : error
                    }