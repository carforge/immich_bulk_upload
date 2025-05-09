# Original code snippet from Immich Documentation
# https://immich.app/docs/guides/python-file-upload
import requests
import os
from datetime import datetime


class immich_uploader():
    def __init__(self, api_key:str, base_url:str):
        self.API_KEY = api_key
        self.BASE_URL = base_url


    def upload(self, file:str):
        stats = os.stat(file)

        headers = {
            'Accept': 'application/json',
            'x-api-key': self.API_KEY
        }

        data = {
            'deviceAssetId': f'{file}-{stats.st_mtime}',
            'deviceId': 'python',
            'fileCreatedAt': datetime.fromtimestamp(stats.st_mtime),
            'fileModifiedAt': datetime.fromtimestamp(stats.st_mtime),
            'isFavorite': 'false',
        }

        files = {
            'assetData': open(file, 'rb')
        }

        response = requests.post(
            f'{self.BASE_URL}/assets', headers=headers, data=data, files=files)

        return response.json()


def is_supported(filename:str):
    file_extensions = [".avif", ".bmp", ".gif", ".heic", ".heif", ".jp2", ".webp", ".jpg", 
                       ".jpe", ".insp", ".jxl", ".png", ".psd", ".raw", ".rw2", ".svg", ".tif", 
                       ".tiff", ".3gp", ".3gpp", ".avi", ".flv", ".m4v", ".mkv", ".mts", ".m2ts", 
                       ".m2t", ".mp4", ".insv", ".mpg", ".mpe", ".mpeg", ".mov", ".webm", ".wmv"]
    return any(filename.lower().endswith(ext.lower()) for ext in file_extensions)