from bs4 import BeautifulSoup
import requests

def download(result):
    download = requests.get(result[0]['href'])
    d_soup = BeautifulSoup(download.raw, 'html.parser')
    return d_soup

def write_file(download):
    with open("test_image.png", 'wb') as fd:
            for chunk in download.iter_content(chunk_size=4096):
                fd.write(chunk)


da_page = requests.get("https://pridark.deviantart.com/gallery/")
soup = BeautifulSoup(da_page.text, 'html.parser')
result = soup.find_all('a', href='https://pridark.deviantart.com/art/Comm-Blue-and-Orange-720560563')
link = result[0]['href']
print("RESULT : ", link)
print("-" * 50)
#download = download(result)
#write_file(download)
print("OK")





