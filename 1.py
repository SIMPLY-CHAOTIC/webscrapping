from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
website="https://finance.yahoo.com/quote/TATAMOTORS.NS/history?period1=1676678400&period2=1708214400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
path=Service("D:/AI Project/Chrome_driver/chromedriver-win64/chromedriver-win64/chromedriver.exe")
opi=Options()
opi.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=path,options=opi)
time.sleep(5)
driver.get(website)

datas=driver.find_elements(By.TAG_NAME,'tr')
i=0
for data in datas:
    if i==0:
        i=i+1
        continue
    else:
        print(data.text)
        break
    