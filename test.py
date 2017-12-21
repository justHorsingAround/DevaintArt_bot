from bs4 import BeautifulSoup
import requests
import json


def download(result):  # dead code
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
    

def search_pictures(url, class_tag, class_name_one, class_name_two, tag_in_list):  # not needed, delete later, json_request will do the job
    DIV = "div"
    soup = fetch_html(url)
    outer_div = soup.find(DIV, class_="torpedo-container")
    result = outer_div.find_all(class_tag, class_=class_name_two)
    links = [item[tag_in_list] for item in result]
    return links


def fetch_csrf(url):
    soup = fetch_html(url)
    all_script = soup.head.find_all('script')
    csrf = ""
    for i in all_script:
        if i.string == None:
            continue
        match_index = i.string.find('csrf')
        if int(match_index) > -1:
            res = i.string.split(",")
            for j in range(len(res)):
                if 'csrf' in res[j]:
                    csrf = res[j].split(":")
                    csrf = [[csrf[i].replace('"', '') for i in range(len(csrf))]]
                    csrf = dict(csrf)
    return csrf

def fetch_src(links):
    INDEX_OF_HI_RES = 0
    INDEX_OF_NAME = -1

    test_set = set()
    test_counter = 1

    for link in links:
        print("NUMBER :: ", test_counter)
        test_counter += 1
        print("FETCHED LINK: ", link)    
        soup_for_img_serach = fetch_html(link)
        out_div = soup_for_img_serach.find("div", class_='dev-view-deviation')
        res = [i for i in out_div.find_all("img", class_='dev-content-full')]
        if not res:
            print("This is not a picture or NSFW content")
            continue
        res = [j['src'] for j in res]
        print("RES ------------------- ", res)
        test_set.update(res)
        split_name = res[INDEX_OF_HI_RES].split('/')
        print("SAVED AS: {} \n".format(split_name[INDEX_OF_NAME]))


        write_file(requests.get(res[INDEX_OF_HI_RES]), split_name[INDEX_OF_NAME])



def make_url(user_name):
    page_url = 'https://'
    page_url += user_name.lower()
    page_url += '.deviantart.com/gallery/?catpath=/'
    return page_url


user_name = "Burgunzik" 

page_url = make_url(user_name)

class_name_one = 'folderview-art'  # dead code 
CLASS_NAME_FOR_TAG_A = 'torpedo-thumb-link'
TAG_A = 'a'
tag_in_list = 'href'  
links = search_pictures(page_url, TAG_A, class_name_one, CLASS_NAME_FOR_TAG_A, tag_in_list)
   

json_request= {
"username" : "",
"offset" : "0",
"limit" : "24",
"_csrf" : "",
"dapiIid" : "0"}

USER_AGEN = "Mozilla/5.0 (Windows NT 10.0;...) Gecko/20100101 Firefox/57.0"
HEADER = {"user_agen" : USER_AGEN}

csrf = fetch_csrf(page_url)
print(csrf)
json_request["username"] = user_name
json_request["_csrf"] = csrf['csrf']
print(json_request)


href_set = set()
offset_counter = 0
temp_counter = 0
while True:
    req = requests.post(page_url, data=json_request, headers=HEADER)
    print("REQUEST --  ", req)
    json_soup = BeautifulSoup(req.text, 'html.parser')
    out_div2 = [i['href'] for i in json_soup.find_all(TAG_A, class_= CLASS_NAME_FOR_TAG_A)]
    if len(out_div2) == 0:
        break
    else:
        href_set.update(out_div2)

    offset_counter += 24
    json_request["offset"] = str(offset_counter)

    temp_counter += 1
    print("TEMP COUNTER ------------------- ", temp_counter)

print(href_set)
print("LEN ---------------- ", len(href_set))

fetch_src(href_set)


print("-" * 50)
print("OK")





