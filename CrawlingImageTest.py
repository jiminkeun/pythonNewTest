from urllib.request import urlopen
from bs4 import BeautifulSoup

# 이미지 다운로드
def download_img(url):
    savePath = "E:/Data/크롤링자료/9seke.com/"
    imgName = url.replace("http://p9.x1994.com/I/","")
    urlopen.urlretrieve(url,savePath+imgName)

url = "http://www.9seke.com/article/html/11396.html"
html = urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html5lib")
img_source = soup.find("div", {"class":"content"}).find_all("img")

#print(img_source)


for img_item in img_source:
    #download_img(img_item.get("src"))
    url = img_item.get("src")
    #urlopen.urlretrieve(url, url.replace("http://p9.x1994.com/I/",""))
    print(img_item.get("src") + " 다운로드 완료 \n")


