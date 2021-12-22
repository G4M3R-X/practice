from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"D:\github_practice\practice\selenium_python\ChromeDriver\chromedriver.exe")

url = "https://www.mail.ru/"
url2 = "https://e.mail.ru/compose/"
login = "test1t@internet.ru"
password = "Dy*upaPYPy32"
try:
    driver.get(url=url)
    time.sleep(2)
    # -------------------
    email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="login-input"]')
    email_input.clear()
    email_input.send_keys(login)
    time.sleep(1)
    # -------------------
    button1 = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="enter-password"]').click()
    time.sleep(3)
    #--------------------
    pass_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
    pass_input.clear()
    pass_input.send_keys(password)
    time.sleep(1)
    # -------------------
    button2 = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="login-to-mail"]').click()
    time.sleep(12)
    # -------------------
    button3 = driver.find_element(By.CSS_SELECTOR, '[title="Написать письмо"]').click()
    # driver.get(url=url2)
    time.sleep(3)
    # -------------------
    email_input2 = driver.find_element(By.CSS_SELECTOR, 'input.container--H9L5q.size_s--3_M-_')
    email_input2.clear()
    email_input2.send_keys(login)
    time.sleep(1)
    # -------------------
    input3 = driver.find_element(By.CSS_SELECTOR, 'input[name="Subject"]')
    input3.clear()
    input3.send_keys("Тестовое письмо")
    time.sleep(1)
    # -------------------
    testletter = driver.find_element(By.CSS_SELECTOR, ".cke_editable_inline.cke_contents_true.cke_show_borders")
    testletter.clear()
    testletter.send_keys("Это тестовое письмо и бла-бла-бла")
    time.sleep(1)

    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.container--2lPGK.type_wide--2kyds.color_base--hO-yz.hoverable--2qtk5')
    buttons[1].click()
    time.sleep(2)

    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()