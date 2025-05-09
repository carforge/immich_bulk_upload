import os
import sys
from helper import immich_uploader, is_supported

API_KEY = ""        # replace with a valid api key
IMMICH_URL = ""     # e.g. http://127.0.0.1:2283/api

my_uploader = immich_uploader(api_key=API_KEY, base_url=IMMICH_URL)


def upload_file(filename:str):
    if is_supported(filename=filename):
        print(my_uploader.upload(file=filename))


def main():
    upload_folder = sys.argv[1]
    print(f"Uploading files from folder: {upload_folder}")

    # Loop over all directories, sub-directories and files
    for dirpath, dirnames, filenames in os.walk(upload_folder):
        print(f'Directory: {dirpath}')
        for dirname in dirnames:
            print(f'Sub-directory: {dirname}')
        for filename in filenames:
            local_file_path = os.path.join(dirpath, filename)
            upload_file(filename=local_file_path)


if __name__ == "__main__":
    main()