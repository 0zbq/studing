import requests
response=requests.get("https://books.toscrape.com/")
if response.ok:
    print("请求成功")
else:
    print("请求失败")
print(response)
print(response.status_code)


response=requests.get("https://movie.douban.com/top250")
if response.ok:
    print("请求成功")
else:
    print("请求失败")
print(response)
print(response.status_code)

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
response=requests.get("https://movie.douban.com/top250",headers=headers)
if response.ok:
    print("请求成功")
else:
    print("请求成功")
print(response)
print(response.status_code)




from bs4 import BeautifulSoup
content=response.text
soup=BeautifulSoup(content,"html.parser")
#print(soup.p)
#print(soup.img)
all_prices=soup.find_all("span",attrs={"class":"title"})
for price in all_prices:
    title=price.string
    if '/' not in title:
        print(title)







