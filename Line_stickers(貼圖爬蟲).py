# -*- coding: utf-8 -*-
"""Line 貼圖爬蟲練習 """

import os , requests ,pprint, json
from bs4 import BeautifulSoup

#新增目錄底下的資料夾
folder = ("line貼圖下載資料夾")
if not os.path.exists(folder):
    os.makedirs(folder)

url = 'https://store.line.me/stickershop/product/24392/'
my_header ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
resp = requests.get(url , headers=my_header) #Get_URL
soup = BeautifulSoup(resp.text,'lxml')  #使用美麗湯
line_element =soup.select('ul.mdCMN09Ul.FnStickerList > li.mdCMN09Li.FnStickerPreviewItem') # 抓到對應的CSS 節點發現是JSON，且有png網站連結

list_line_stickers=[]
for line in line_element:
    strJson =line['data-preview']
    obj=json.loads(strJson)  #載入JSON，但因為多個所以要加S
    
    # 分成 ID 以及 PNG檔案的URL 以便等等使用CURL
    list_line_stickers.append({
        'id' : obj['id'],
        'staticUrl': obj ['staticUrl']        
    })

for obj in list_line_stickers:
    os.system(f" curl {obj['staticUrl']} -o{folder}/{obj['id']}.png")  #使用CURL連結到該網站後，另存至帶有ID.png
    print(f" 貼圖: {obj['id']}, 連結: {obj['staticUrl']}")