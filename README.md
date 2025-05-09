# Immich Bulk Uploader

A Python tool to upload a large number of images to an Immich instance. This tool uses the original Python code from the Immich documentation and checks if the file is supported by Immich according to the supported media types list in the Immich documentation.

## Features

- Uploads a large number of images to an Immich instance.
- Checks if the file is supported by Immich.
- Provides statistics on uploaded and skipped files.

## Prerequisites

- Python 3.x
- `requests` library
- An Immich instance with a valid API key

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/immich-bulk-uploader.git
    cd immich-bulk-uploader
    ```

2. Install the required dependencies:

    ```sh
    pip install requests
    ```

## Usage

1. Replace the `API_KEY` and `IMMICH_URL` variables in the script with your actual Immich API key and URL.

    ```python
    API_KEY = "your_api_key"        # replace with a valid api key
    IMMICH_URL = "http://127.0.0.1:2283/api"     # e.g. http://127.0.0.1:2283/api
    ```

2. Run the script with the path to the folder containing the images you want to upload:

    ```sh
    python immich_bulk_uploader.py /path/to/your/images
    ```

## Code Explanation

- `immich_uploader`: A helper class to handle the upload process.
- `is_supported`: A helper function to check if a file is supported by Immich.
- `upload_file`: Uploads a single file to Immich if it is supported.
- `main`: The main function that loops over all directories, sub-directories, and files, and uploads them to Immich.

## Example Output

```sh
Uploading files from folder: /path/to/your/images
Directory: /path/to/your/images
Sub-directory: subdir1
image1.jpg:
{'status': 'success', 'message': 'File uploaded successfully'}
image2.png:
{'status': 'skipped', 'message': 'File type not supported'}
Processed 2 files. 1 have been added to Immich, 1 have been skipped.