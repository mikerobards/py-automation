from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# service = Service(executable_path='./chromedriver')
service = Service(ChromeDriverManager().install())

options = Options()
# this ensures chrome window does not close
options.add_experimental_option('detach', True)

chrome_browser = webdriver.Chrome(service=service, options=options)

print(chrome_browser)

chrome_browser.maximize_window()
