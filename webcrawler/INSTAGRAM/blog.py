from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

옵션 = webdriver.ChromeOptions()
# chrome://version 입력해서 프로필 경로 가져와서 복붙
옵션.add_argument(r'user-data-dir=C:\Users\jisung\AppData\Local\Google\Chrome\User Data\Default') 
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')

time.sleep(2)

pyperclip.copy('chuchun4999')
e = driver.find_element(By.CSS_SELECTOR,'#id')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)

pyperclip.copy('비번')
e = driver.find_element(By.CSS_SELECTOR,'#pw')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)
e.send_keys(Keys.ENTER)
