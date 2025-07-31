import requests
from bs4 import BeautifulSoup
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
num=1
for i in range(1,6):
    responses=requests.get(f"https://www.acwing.com/problem/{i}/?show_algorithm_tags=0&show_accepted_problems=none",headers=headers)
    html=responses.text
    contents=BeautifulSoup(html,"html.parser")
    all_title=contents.find_all("a",attrs={"target":"_blank"})
    for title in all_title:
        print(num)
        print(title.string)
        num=num+1