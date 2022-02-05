""" Use selenuim to combine news results from google news """

'''匯入套件'''
# 操作 browser 的 API
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# 強制等待 (執行期間休息一下)
from time import sleep
import pandas as pd 



#命名Webdriver 
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options= option)

#如需要在Google Chrome瀏覽器下指令保持Google帳號登入狀況 
# chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\Users\User\api\localhost

#新聞標題
News_title=[]
# 作者/報社
Author=[]
# 連結
Link =[]
# 內容
Content=[]
# 設定你想要爬的頁數
Page = 20


def clickhomepage():
    driver.get('https://www.google.com'); #Google網站
    sleep(2)
    Search = driver.find_element(By.CSS_SELECTOR,'input.gLFyf.gsfi') #點登記按鈕
    Search.send_keys("搜尋你想要的結果")
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input.gNO89b").click()   
    sleep(3)
    driver.find_element_by_link_text("新聞").click()
    sleep(2)


# 分析頁面元素資訊
def parse():
    # 取得主要元素的集合
    # 取得標題 & 連結
    
    for i in range(0,Page):
        try:
            if i == i:
                Links = driver.find_elements(By.CSS_SELECTOR,'a.WlydOe') # 取的新聞連結
                for link in Links:
                    H =link.get_attribute('href')
                    Link.append(H)
                
   
                Authors = driver.find_elements(By.CSS_SELECTOR, 'div.CEMjEf.NUnG9d')# 取得新聞媒體報社
                for author in Authors:
                    N =author.get_attribute('innerText')
                    Author.append(N)
                
                Contents = driver.find_elements(By.CSS_SELECTOR,'div.GI74Re.nDgy9d')# 取得簡易內容
                for content in Contents:
                    N =content.get_attribute('innerText')
                    Content.append(N)
                
                News = driver.find_elements(By.CSS_SELECTOR,'div.mCBkyc.y355M.JQe2Ld.nDgy9d') #取得新聞標題
                for new in News:
                    N =new.get_attribute('innerText')
                    News_title.append(N)                
                sleep(1)
                driver.find_element_by_link_text("下一頁").click()
        except(Exception): #例外處理
            print(f'第{i}頁已到盡頭爬蟲結束')
            break

            
if __name__ == '__main__':
    clickhomepage()
    parse()

#合併成Datafram 再轉成Csv
News = pd.DataFrame(News_title, columns=['新聞標題'])
News['新聞簡短內容']=pd.DataFrame(Content)
News['報社/作者'] =pd.DataFrame(Author)
News['連結']=pd.DataFrame(Link)
News.to_csv('New.csv')


