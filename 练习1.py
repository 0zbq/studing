import requests
from bs4 import BeautifulSoup

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
for i in range(0,250,25):
    responses=requests.get(f"https://movie.douban.com/top250?start={i}&filter=",headers=headers)
    contents=responses.text
    soup=BeautifulSoup(contents,"html.parser")
    all_title=soup.find_all("span",attrs={"class":"title"})
    for title in all_title:
        if '/' not in title.string:
            print(title.string)