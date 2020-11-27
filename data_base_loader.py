from tqdm import tqdm
import requests
import os


class DataBase:
    def __init__(self, db_file_path, db_url, force):
        self.db_file_path = db_file_path
        self.db_url = db_url
        if force or not self.check_xml():
            self.load_xml()

    def check_xml(self):
        return os.path.exists(self.db_file_path)

    def load_xml(self):
        # Streaming, so we can iterate over the response.
        response = requests.get(self.db_url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte

        progress_bar = tqdm(total=total_size_in_bytes, unit='iB',
                            unit_scale=True)
        with open(self.db_file_path, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("Error, something went wrong")
