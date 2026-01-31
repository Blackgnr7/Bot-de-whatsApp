from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

driver = None

def get_driver():
    global driver
    if driver is None:
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
    return driver
