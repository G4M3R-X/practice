from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"D:\github_practice\practice\selenium_python\ChromeDriver\chromedriver.exe")

url = "https://www.vk.com/"

try:
    driver.get(url=url)
    time.sleep(5)
    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("+79670333350")
    time.sleep(3)
    # -------------------
    pass_input = driver.find_element_by_id("index_pass")
    pass_input.clear()
    pass_input.send_keys("GaryGuls")
    time.sleep(3)
    # -------------------
    button = driver.find_element_by_id("index_login_button").click()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
