from appium import webdriver

def create_driver(capabilities):
    return webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
