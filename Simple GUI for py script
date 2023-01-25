import os
import re
import requests
import urllib.request
import tkinter as tk
from tkinter import filedialog

def check_url(url):
    match = re.match(r"https://heritage\.canadiana\.ca/view/oocihm\.lac_reel", url)
    return match

def download_pages():
    #DL folder
    folder = folder_entry.get()
    script_path = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(script_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print("Files will be downloaded in '%s' " % folder_path)

    #URL du reel
    url = url_entry.get()
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

root = tk.Tk()
root.title("Download Pages")

folder_label = tk.Label(root, text="Enter a foldername: ")
folder_label.pack()

folder_entry = tk.Entry(root)
folder_entry.pack()

url_label = tk.Label(root, text="Enter a URL: ")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=download_pages)
download_button.pack()

root.mainloop()
