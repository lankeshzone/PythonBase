from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = ""
pwd = ""
driver = webdriver.Firefox()
#driver2 = webdriver.Firefox()
driver2 = webdriver.Chrome()
driver2.get("https://www.google.co.in")
search = driver2.find_element_by_name("q")


search.send_keys("lankesh")
assert "true" in search.is_displayed()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#driver.close()