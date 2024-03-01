from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:/Users/rajni/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')

link = driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
driver.execute_script("arguments[0].click();", link)

link2 = driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]')
driver.execute_script("arguments[0].click();", link2)

time.sleep(3)
# link = driver.execute_script(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
# link.click()

old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    load_more = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div[3]')
    driver.execute_script("arguments[0].click();", load_more)

    time.sleep(3)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html','w',encoding="utf-8") as f:
    f.write(html)
time.sleep(10)