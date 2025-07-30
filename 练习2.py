import requests
from bs4 import BeautifulSoup
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
for i in range(0,250,25):
    responses=requests.get(f"https://book.douban.com/top250?start={i}",headers=headers)
    contents=responses.text
    soup=BeautifulSoup(contents,"html.parser")
    all_title1=soup.find_all("div",attrs={"class":"pl2"})
    for all_title in all_title1:
        title=all_title.a
        if  title.string!=None :
            print(title.string)







