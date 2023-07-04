import webbrowser
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import msvcrt

service = Service(executable_path="D:/webDrivers")


df = pd.read_csv("20170308hundehalter.csv")
all_breeds = [i for i in df['RASSE1'].drop_duplicates()]

# print(len(breeds))
# print((breeds))


top_breed = df['RASSE1'].value_counts()
bottom_breed = df['RASSE1'].value_counts().tail(10)

options = webdriver.ChromeOptions()
browser = uc.Chrome()
browser.get("https://google.com")

# print(bottom_breed.index)
# for i in range(15,21):
for i in bottom_breed.index:
# 	i = bottom_breed.index[i]
	print(i)
	path = f"https://google.com/search?q={i} dog price"
	path = path.replace(" ", "%20")
	browser.get(path)
	msvcrt.getch()
print(len(all_breeds))