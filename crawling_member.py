import requests

page = 1
last_page = 36
def crawling(url,f_path):
    global page,last_page
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}  #firefoxに偽装
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    filename = f_path + ".html"
    with open(filename,'w',encoding="utf-8") as f:
        f.write(response.text)
    print(page)
    while page < last_page:
        pre_p = page
        page += 1
        nexturl = url[:-1]
        nexturl += str(page)
        f_path = f_path.replace(str(pre_p),str(page))
        crawling(nexturl,f_path)    #再帰

if __name__ == "__main__":
    url = "http://sp.senkyo.mainichi.jp/giin/list.html?p=1"
    filename = "diet-member_1"
    crawling(url,filename)