from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
import time
from selenium.webdriver.common.by import By

# 영화검색어 입력
search_keyword = "보통사람"

# DB 커넥션
conn = pymongo.MongoClient("localhost")
db_movie = conn.movie
tb_mvInfo = db_movie.movle_info

# 함수 모음
def setMvInfo(source):
    soup = BeautifulSoup(source, "html5lib")
    source = soup.find("div", {"class": "mv_info_area"})
    title_kor = source.find("div", {"class": "mv_info"}).find("a").text
    title_eng = source.find("div", {"class": "mv_info"}).find("strong", {"class": "h_movie2"}).text
    img_url = source.find("div", {"class": "poster"}).find("img").get("src")
    doc = {'no':'1','title_kor':title_kor, 'title_eng':title_eng, 'img_url':img_url}
    tb_mvInfo.insert(doc)

def getMvInfo():
    result = tb_mvInfo.find()
    for r in result:
        print(r+"\n")

# 파이어폭스 WebDriver를 이용해 firefox를 실행.
driver = webdriver.Firefox(executable_path='E:/Dev/tool/geckodriver-v0.21.0-win64/geckodriver.exe')
driver.get("https://movie.naver.com/")
driver.implicitly_wait(1)

# html element ID가 ipt_tx_srch인 것을 찾습니다. (검색창)
inputElement = driver.find_element_by_id("ipt_tx_srch")

# 검색창에 '영화검색어'를 입력합니다.
inputElement.send_keys(search_keyword)
driver.implicitly_wait(1)

# 검색 버튼을 클릭
driver.find_element_by_class_name("btn_srch").click()
driver.implicitly_wait(1)

# 검색된 리스트 중 링크 텍스트에 '영화검색어' 포함된 것 중 1번째것을 찾습니다.
continue_link = driver.find_element_by_partial_link_text(search_keyword)
driver.implicitly_wait(1)

# 해당 링크를 클릭합니다.
continue_link.click()
# 해당 화면의 모든 소스 가져오기
source = driver.page_source

# 영화 정보 가져오기
setMvInfo(source)

getMvInfo()
driver.implicitly_wait(1)


# WebDriver를 종료합니다. (브라우저 닫기)
driver.quit()




'''
# 이미지 다운로드
def download_img(url):
    savePath = "E:/Data/크롤링자료/"
    imgName = url.replace("https://movie.naver.com/movie/bi/mi/","")
    urlopen.urlretrieve(url,savePath+imgName)

url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=140652"
html = urlopen(url)
source = html.read()
html.close()

soup = BeautifulSoup(source, "html5lib")
source = soup.find("div", {"class":"mv_info_area"})
title_kor = source.find("div", {"class":"mv_info"}).find("a").text
title_eng = source.find("div", {"class":"mv_info"}).find("strong", {"class":"h_movie2"}).text
img_url = source.find("div", {"class":"poster"}).find("img").get("src")

print(title_kor+"\n"+title_eng+"\n"+img_url)

#urlopen.urlretrieve(img_url, title_kor+".jpg")
'''



