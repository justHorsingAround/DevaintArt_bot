from bs4 import BeautifulSoup
import requests

def download(result):
    download = requests.get(result[0]['href'])
    return download

def write_file(download, file_name):
    with open(file_name, 'wb') as fd:
            for chunk in download.iter_content(chunk_size=4096):
                fd.write(chunk)

def fetch_html(page_url):
    da_page = requests.get(page_url)
    mysoup = BeautifulSoup(da_page.text, 'html.parser')
    return mysoup
    

page_url = 'https://lulemt.deviantart.com/gallery/'
soup = fetch_html(page_url)
outer_div = soup.find("div", class_='folderview-art')
result = outer_div.find_all("a", class_="torpedo-thumb-link")
links = [item['href'] for item in result]

INDEX_OF_HI_RES = 0
INDEX_OF_NAME = -1
for link in links:
    print("FETCHED LINK: ", link)    
    url = fetch_html(link)
    out_div = url.find("div", class_='dev-view-deviation')
    res = [i['src'] for i in out_div.find_all("img", class_='dev-content-full')]
    split_name = res[INDEX_OF_HI_RES].split('/')
    print("SAVED AS: {} \n".format(split_name[INDEX_OF_NAME]))
    
    write_file(requests.get(res[INDEX_OF_HI_RES]), split_name[INDEX_OF_NAME])


print("-" * 50)
print("OK")





