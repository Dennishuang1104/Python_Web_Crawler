import os ,json , requests ,re
from bs4 import BeautifulSoup
import time
import re 
import pandas as pd 
import numpy as np

SaveCarDF= pd.DataFrame(columns=["年份","品牌","車子名稱","價格","顏色","cc數","幾門","所在城市"]) #建立DataFrame
Yearlist=[]     #年份
CarBrandlist=[] #品牌
Carlist=[]      #車子名稱
Pricelist=[]    #價格
Colorlist=[]    #顏色
CClist=[]       #CC數名稱
Citylist=[]     #所在城市
Mileslist=[]     #里程數

def get_elements(example):   #取得元素的函式
    examples = [node.text for node in example][0]
    return examples


for i in range (99999,203095):
    try:
        if i <100000:
            url = f"https://www.isave.com.tw/car.aspx?cid=0{i}"
            my_headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
            time.sleep(np.random.uniform(0.3,1.2)) # 隨機睡眠1-2秒
            resp = requests.get(url , headers = my_headers)
            soup= BeautifulSoup(resp.text)
            Yearnodes= soup.select(selector='.clearfix:nth-child(4) .option-content',features= "html.parser")#找年份
            Brandnodes= soup.select(selector='.clearfix:nth-child(2) .option-content',features= "html.parser")#找品牌
            Carnamenodes= soup.select(selector='.clearfix:nth-child(3) .option-content',features= "html.parser")#找車款名
            Pricenodes= str(soup.select(selector='.price',features= "html.parser")) #價格
            Colornodes = soup.select(selector='.clearfix:nth-child(6) .option-content',features= "html.parser") #找顏色
            CCnodes = soup.select(selector='.clearfix:nth-child(8) .option-content',features= "html.parser") #CC數名稱
            Citynodes = soup.select(selector='.clearfix:nth-child(5) .option-content',features= "html.parser") #所在城市
            Milesnodes = soup.select(selector='.clearfix:nth-child(9) .option-content',features= "html.parser") #里程數
            
            if  re.findall(r'[0-9.]+\s萬', Pricenodes)[0] ==[]:     #如果沒有價格就Pass
                print(f"第{i}筆資料已經成交")
                pass
                
            else:
                Year =get_elements(Yearnodes)    #找年份
                Yearlist.append(Year)
                Brand =get_elements(Brandnodes)     #找品牌
                CarBrandlist.append(Brand)
                Carname =get_elements(Carnamenodes) #找品牌與汽車名稱
                Carlist.append(Carname)
                Price=re.findall(r'[0-9.]+\s萬', Pricenodes)[0]            #找價格
                Pricelist.append(Price)
                Color= get_elements(Colornodes)   #找顏色
                Colorlist.append(Color)
                CC= get_elements(CCnodes) #找CC數
                CClist.append(CC)
                Miles= get_elements(Milesnodes) #找r幾門
                Mileslist.append(Miles)  
                City= get_elements(Citynodes) #找所在城市
                Citylist.append(City)
                print(f"第{i}筆完整資料載入完成")
        else:
            url = f"https://www.isave.com.tw/car.aspx?cid={i}"
            my_headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
            time.sleep(np.random.uniform(0.3,1.2)) # 隨機睡眠1-2秒
            resp = requests.get(url , headers = my_headers)
            soup= BeautifulSoup(resp.text)
            Yearnodes= soup.select(selector='.clearfix:nth-child(4) .option-content',features= "html.parser")#找年份
            Brandnodes= soup.select(selector='.clearfix:nth-child(2) .option-content',features= "html.parser")#找品牌
            Carnamenodes= soup.select(selector='.clearfix:nth-child(3) .option-content',features= "html.parser")#找車款名
            Pricenodes= str(soup.select(selector='.price',features= "html.parser")) #價格
            Colornodes = soup.select(selector='.clearfix:nth-child(6) .option-content',features= "html.parser") #找顏色
            CCnodes = soup.select(selector='.clearfix:nth-child(8) .option-content',features= "html.parser") #CC數名稱
            Citynodes = soup.select(selector='.clearfix:nth-child(5) .option-content',features= "html.parser") #所在城市
            Milesnodes = soup.select(selector='.clearfix:nth-child(9) .option-content',features= "html.parser") #里程數
            
            if  re.findall(r'[0-9.]+\s萬', Pricenodes)[0] ==[]:     #如果沒有價格就Pass
                print(f"第{i}筆資料已經成交")
                pass
                
            else:
                Year =get_elements(Yearnodes)    #找年份
                Yearlist.append(Year)
                Brand =get_elements(Brandnodes)     #找品牌
                CarBrandlist.append(Brand)
                Carname =get_elements(Carnamenodes) #找品牌與汽車名稱
                Carlist.append(Carname)
                Price=re.findall(r'[0-9.]+\s萬', Pricenodes)[0]            #找價格
                Pricelist.append(Price)
                Color= get_elements(Colornodes)   #找顏色
                Colorlist.append(Color)
                CC= get_elements(CCnodes) #找CC數
                CClist.append(CC)
                Miles= get_elements(Milesnodes) #找r幾門
                Mileslist.append(Miles)  
                City= get_elements(Citynodes) #找所在城市
                Citylist.append(City)
                print(f"第{i}筆完整資料載入完成")
     
    except(Exception):
        print(f'第{i}筆發生錯誤')

SaveCarDF["年份"] = Yearlist
SaveCarDF["品牌"] = CarBrandlist
SaveCarDF["車子名稱"]= Carlist
SaveCarDF["價格"]= Pricelist
SaveCarDF["顏色"]= Colorlist
SaveCarDF["cc數"]= CClist
SaveCarDF["里程數"]=Mileslist
SaveCarDF["所在城市"]=Citylist

SaveCarDF.to_csv("Savecar_info.csv")