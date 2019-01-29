import re,sys
from bs4 import BeautifulSoup

def scrape(search_n):
    re_sub = re.compile(r'[︰-＠]')  #全角記号
    for page in range(1,100):
        try:
            html = open("pages/diet-member_{}.html".format(page),'r')
        except FileNotFoundError:
            break
        soup = BeautifulSoup(html, "html.parser")
        for res in soup.find_all(class_="ContentsData"):
            name = res.find(class_="Name").text.replace('\u3000','')    #タブを削除
            name = re_sub.sub(' ',name) #カッコを取り除く
            name = name.split(' ')  #リスト化（名前、年齢、読み仮名）
            if name[0] == search_n or name[2] == search_n:
                party = res.find(class_="Party").text
                print(party)
                return 0
    #return 

if __name__ == "__main__":
    name = sys.argv[1]
    scrape(name)