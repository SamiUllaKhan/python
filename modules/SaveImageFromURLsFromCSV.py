# Imports
import os
import pandas as pd
import urllib.request

# Main function to read and save Images
def url_to_jpg(i, url, file_path):
    filename = '{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))
    return None


# Config
FILE_NAME = "Book1.csv"
FILE_PATH = "Images/"

# Read data from list
urls = pd.read_csv(FILE_NAME)

# Calling function in the loop with image URL
for i, url in enumerate(urls.values):
    url_to_jpg(os.path.splitext(os.path.basename(url[0]))[0], url[0], FILE_PATH)
