import webbrowser
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="D:/webDrivers")
import msvcrt

options = webdriver.ChromeOptions() 
browser = uc.Chrome()
browser.get("https://google.com")

links = [
	'https://www.mydogcompany.com',
	'https://citydogs.ch/en/',
	'https://dogaffair.ch/en/booking',
	'https://www.dog2dog.ch/kontakt/',
	'https://hundeschule-glattpark.ch',
	'https://pawhouse.ch',
	'https://hundeabenteuerland.ch',
	'https://www.walking-dogs.ch/en/',
	'https://fit-dogs.ch',
	'https://www.maykesdogwalk.ch',
	'https://www.citypet.ch/english/',
	'http://www.happy-hundehort.ch',
	'https://woofwoof.ch',
	'https://www.happywalkshappydogs.ch',
	'https://www.holydog.ch',
	'https://www.dog-knowhow.ch',
	'https://hotdoggrooming.ch',
	'https://www.hundundco.ch',
	'https://www.doggiesway.ch/kontakt',
	'https://dogparkcare.ch',
	'https://wholetthedogsout.ch',
	'https://www.dogcareplus.ch/',
	'https://www.dold-dog.ch',
	'https://www.smilingdogs.ch',
]

bussiness_names = []
for i in links:
	# i = i.replace("/", "")
	# i = i.replace(":", "")
	# i = i.replace("https", "")
	i = i.replace("www.", "")
	indx = i.rindex("://")
	i = i[indx+3:]
	indx = i.rindex(".")
	print(i[:indx])
	bussiness_names.append(i[:indx])
	# break

for i in bussiness_names:
	print()
	print(i)
	# path = f"https://google.com/search?q={i}"
	path = f"https://google.com/search?q={i}%20zurich"
	print(path)
	browser.get(path)
	# address_element = driver.find_element_by_css_selector("div span[data-local-attribute='d3adr']")
	# address_text = address_element.text
	
	address = None
	try:
		address = browser.find_element(By.CLASS_NAME, "LrzXr")
		print(address.get_attribute("outerHTML"))
	except:
		print("no addr")

	# phone = None
	# try:
	# 	phone = browser.find_element(By.CLASS_NAME, "fl")
	# 	# xpath = '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[7]/div/div/div/span[2]/span/a/span'
	# 	# xpath = '/html/body/div[6]/div/div[13]/div[2]/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div[8]/div/div/div/span[2]/span/a/span'
	# 	# # phone = browser.find_element(By.xpath(xpath))
	# 	# phone = browser.find_elements_by_xpath(xpath)
	# 	# print(phone.get_attribute("outerHTML"))
	# except:
	# 	print("no phone")

	# msvcrt.getch()

print("end")
msvcrt.getch()
