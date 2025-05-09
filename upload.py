import os
import sys
from helper import immich_uploader, is_supported


API_KEY = "your_api_key"                    # replace with a valid api key
IMMICH_URL = "http://127.0.0.1:2283/api"    # replace with a valid immich url
my_uploader = immich_uploader(api_key=API_KEY, base_url=IMMICH_URL)

stat_uploaded = 0
stat_skipped = 0


def upload_file(filename:str):
    if is_supported(filename=filename):
        global stat_uploaded
        print(f"{my_uploader.upload(file=filename)}")
        stat_uploaded += 1
    else:
        global stat_skipped
        stat_skipped += 1
        

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
            print(f"{filename}:")
            upload_file(filename=local_file_path)    
    print(f"Processed {stat_skipped+stat_uploaded} files. {stat_uploaded} have been added to Immich, {stat_skipped} have been skipped.")


if __name__ == "__main__":
    main()