import os
import re
import requests
import urllib.request

#DL folder
folder = input("Enter a foldername: ")
script_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(script_path, folder)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
print("Files will be downloaded in '%s' " % folder_path)

#URL du reel
url = input("Enter a URL (ex:https://www.ebay.de/itm/125016241453?hash=item1d1b8c752d:g:r7kAAOSwl-5hnMmH): ")

response = requests.get(url)
source = response.text

# Find all URLs in the source code that contain "/info.json"
urls = re.findall(r'(https?://[^\s]+/s-l1600.jpg)', source)
count = len([x for x in urls if x.startswith('http')])
print(urls)
title_search = re.search(r'<title>(.*?)</title>', source)
description_search = re.search(r'<meta name="description" content="(.*?)"', source)

if title_search:
    title = title_search.group(1)
else:
    title = None

if description_search:
    description = description_search.group(1)
else:
    description = None

print("Title: ", title)
print("Description: ", description)
print(f"{count} images to download")
input("Press Enter to continue...")
#download all the pages
for i, url in enumerate(urls):
    response = urllib.request.urlopen(url)
    file_name = f"image {i+1}"
    with open(f"{folder}/{file_name}.jpg", "wb") as f:
        f.write(response.read())
    print(f"{file_name}/{count} : OK!")
