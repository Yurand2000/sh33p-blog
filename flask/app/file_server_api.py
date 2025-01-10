import requests

class FileServerAPI:
    def __init__(self):
        import os
        self.host = os.environ['FILE_SERVER_ADDR']
        self.data_folder = "app_data"

    def get_file(self, filename: str):
        response = requests.get(f"http://{self.host}/files/{self.data_folder}/{filename}")
        if response.status_code == 200:
            return response.content
        else:
            return None
        
    def file_exists(self, filename: str):
        response = requests.head(f"http://{self.host}/files/{self.data_folder}/{filename}")
        return response.status_code == 200
    
    def upload_file(self, filename: str, content: bytes, overwrite : bool = False):
        data = {
            'file': content,
            'overwrite': overwrite
        }
        response = requests.put(f"http://{self.host}/files/{self.data_folder}/{filename}", data=data)
        return response.status_code == 200
