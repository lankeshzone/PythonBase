#import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#dir = os.path.dirname("C:\")
#driverIR = webdriver.ie(dir)

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.maximize_window()

googleText = driver.find_element_by_name("q")
googleText.send_keys("Hello")

googleSubmit =  driver.find_element_by_class_name("gNO89b")
googleSubmit.submit()

#Selecting value from Drop Down
element = Select(driver.find_element_by_id('id_of_element'))
element.select_by_index(2)

print("Title is" , driver.title)
print("URL is " , driver.current_url)