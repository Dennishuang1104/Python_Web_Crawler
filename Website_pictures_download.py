# -*- coding: utf-8 -*-
"""網購網站圖片下載"""
import os, requests,time,json,re
from bs4 import BeautifulSoup

#修改Header 造訪網站時不會被抓到
my_headers ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

#建立資料夾名稱
folder = ('PB_website')

img=[]
a=0
for i in range (1,5):
    url=f'https://www.powerbuilt-tw.net/products?page={i}'
    resp = requests.get(url , headers=my_headers)
    soup = BeautifulSoup(resp.text,'lxml')
    ul_element = soup.select("div.boxify-image-wrapper")
    for ul in ul_element:
        Img = str(ul.contents)
        img.append(Img)
#為了正規表達式使用全部轉成字串
str_img =str(img)
PB_image = re.findall(r'[https://shoplineimg.com]+[\/a-zA-Z0-9]+[\.jpg]{4}',str_img)

#創建資料夾，如果沒有此名稱則新增
if not os.path.exists(folder):
    os.makedirs(folder)
    
n=0
for img in PB_image:  #將圖片存入資料夾
    os.system(f" curl {img} -o{folder}/{a}.jpg")
    n=n+1
    