from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json



path = "C:\\Users\\spencer.craigie\\OneDrive\\Documents\\Coding Projects\\Python\\Web Scraping\\chromedriver.exe"
driver = webdriver.Chrome(path)

#driver.get(new_website)

#----------------------------------------#
new_website = "https://dailyharvard.wordpress.com/2021/06/03/december-31/"
d = 365
day = {}

while d != 0:
	driver.get(new_website)
	title = driver.find_element_by_class_name("entry-title")


	text = driver.find_element_by_class_name("entry-content")

	elems = driver.find_elements_by_css_selector(".nav-previous [href]")
	links = [elem.get_attribute('href') for elem in elems]
	

	day[d] = []
	day[d].append({
		"title" : title.text,
		"text" : text.text,
		"link" : links
		})

	with open ('content.json', 'w') as cont:
		json.dump(day, cont, indent=2)

	
	new_website = links[0]
	print(new_website)
	d -= 1



