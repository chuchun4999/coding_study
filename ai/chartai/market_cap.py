import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)