from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('C:\\Users\\User\\AppData\\Local\\Temp\\_AZTMP0_\\chromedriver.exe')
url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
driver.get(url)
html = driver.page_source
df = pd.read_html(html)

print(df[0].dropna(axis=0))