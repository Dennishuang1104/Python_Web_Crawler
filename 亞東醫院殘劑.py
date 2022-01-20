from selenium import webdriver
# 處理逾時例外的工具
from selenium.common.exceptions import TimeoutException
# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait
# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC
# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By
# 強制等待 (執行期間休息一下)
from time import sleep



#解決go
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options= option)

#需要在Google Chrome瀏覽器下指令保持Google帳號登入狀況 
#chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\Users\User\api\localhost

def clickhomepage():
    driver.get('https://hos.femh.org.tw/newfemh/webreg_net/vacccontent.aspx'); #亞東主畫面
    sleep(0.7)
    driver.find_element(By.CSS_SELECTOR,'input[name="Button6"].button').click() #點登記按鈕
    sleep(0.7)
    driver.find_element(By.CSS_SELECTOR,'span.appsMaterialWizButtonPaperbuttonContent.exportButtonContent').click() #表單提交
    sleep(0.6)
    driver.find_element(By.CSS_SELECTOR,'a').click() #點連結繼續
    #----------------------------------------------------------------------------------------------------------------
    sleep(1)
    a= driver.find_elements(By.CSS_SELECTOR,'div.appsMaterialWizToggleRadiogroupEl.exportToggleEl') #選項用迴圈處理 
    for b in range(0,len(a)):
        a[b].click()
        sleep(0.15)
    sleep(0.7)
    
    driver.find_element(By.CSS_SELECTOR,'span.appsMaterialWizButtonPaperbuttonContent.exportButtonContent').click()  #第二頁完成
    #----------------------------------------------------------------------------------------------------------------
    sleep(0.8)
    t=  driver.find_elements(By.CSS_SELECTOR,'div.quantumWizTextinputPaperinputEl.freebirdFormviewerComponentsQuestionTextShort.freebirdFormviewerComponentsQuestionTextTextInput.freebirdThemedInput.modeLight')
    a = driver.find_elements(By.CSS_SELECTOR,'input[type="text"]')
    for x in range(0,len(t)):
        if x ==0:
            t[x].click()
            sleep(0.2)
            a[x].send_keys("黃昱凱")  #填入名字
            sleep(0.3)
        elif x ==1:
            t[x].click()
            sleep(0.2)
            a[x].send_keys("0988706946") #填入手機
            sleep(0.3)
        elif x ==2:
            t[x].click()
            sleep(0.2)
            a[x].send_keys("AXXXXXXXX") #填入身分證字號 
            sleep(0.3)
        elif x ==3:
            t[x].click()
            sleep(0.2)
            a[x].send_keys("28") # 填入年紀
            sleep(0.3)

if __name__ == '__main__':
    clickhomepage()
