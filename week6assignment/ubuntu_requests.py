import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url, content):
    """
    Extract filename from the URL.
    If no filename is present, generate one using a hash of the content.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

# if URL does not contain a file name
    if not filename:  
        file_hash = hashlib.md5(content).hexdigest()[:8]
        filename = f"downloaded_image_{file_hash}.jpg"

    return filename


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # get one or multiple URLs from user
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()

    # create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            # respect: tell the user which URL we're working on
            print(f"\nFetching: {url}")

            # fetch the image with a timeout
            headers = {"User-Agent": "UbuntuFetcher/1.0"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # check for content type
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped: {url} (not an image, Content-Type={content_type})")
                continue

            # extract or generate filename
            filename = get_filename_from_url(url, response.content)

            # prevent duplicates: check if already exists
            filepath = os.path.join("Fetched_Images", filename)
            if os.path.exists(filepath):
                print(f"✗ Duplicate skipped: {filename}")
                continue

            # save image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
