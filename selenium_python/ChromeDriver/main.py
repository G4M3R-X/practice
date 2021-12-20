from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\\github_practice\\practice\\selenium_python\\ChromeDriver\\chromedriver.exe")

url = "https://www.vk.com/"

try:
    driver.get(url=url)
    time.sleep(5)
    driver.get
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
