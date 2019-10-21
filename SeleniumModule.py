from selenium import webdriver
class selDriver:
    def __init__(self):
        self.driver = webdriver.Firefox()
    def launch(self):
        self.driver.get("https://www.google.co.in")

    def close(self):
        self.driver.close()


class selChrome:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def launch(self):
        self.driver.get("https://www.google.co.in")

    def close(self):
        self.driver.close()