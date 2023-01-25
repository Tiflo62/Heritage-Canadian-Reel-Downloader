import os
import re
import requests
import urllib.request

def check_url(url):
    match = re.match(r"https://heritage\.canadiana\.ca/view/oocihm\.lac_reel", url)
    return match

#dossier de DL
folder = input("Enter a foldername: ")
if not os.path.exists(folder):
    os.makedirs(folder)
print("Files will be downloaded in '% s' folder" % folder)

#URL du reel
url = input("Enter a URL (ex:https://heritage.canadiana.ca/view/oocihm.lac_reel_t10533/1): ")
while not check_url(url):
    print("URL does not follow the specified rule. Please try again.")
    url = input("Enter a URL: ")

response = requests.get(url)
source = response.text

# Find all URLs in the source code that contain "/info.json"
urls = re.findall(r'(https?://[^\s]+/info\.json)', source)
modified_urls = [u.replace("/info.json", "/full/max/0/default.jpg") for u in urls]
count = len([x for x in modified_urls if x.startswith('http')])
print(f"{count} pages to download")

input("Press Enter to continue...")
#download all the pages
for i, url in enumerate(modified_urls):
    response = urllib.request.urlopen(url)
    file_name = f"page {i+1}"
    with open(f"{folder}/{file_name}.jpg", "wb") as f:
        f.write(response.read())
    print(f"{file_name}/{count} : OK!")
