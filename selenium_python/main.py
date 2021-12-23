from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"ChromeDriver\chromedriver.exe")

url = "https://www.mail.ru/"
login = "test1t@internet.ru"
password = "Dy*upaPYPy32"
try:
    driver.get(url=url)
    time.sleep(2)
    # Ввод логина
    email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="login-input"]')
    email_input.clear()
    email_input.send_keys(login)
    time.sleep(1)
    # Нажатие на кнопку "Ввести пароль"
    button1 = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="enter-password"]').click()
    time.sleep(3)
    # Ввод пароля
    pass_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="password-input"]')
    pass_input.clear()
    pass_input.send_keys(password)
    time.sleep(1)
    # Нажатие на кнопку "Войти"
    button2 = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="login-to-mail"]').click()
    time.sleep(12)
    # Нажатие на "Написать письмо"
    button3 = driver.find_element(By.CSS_SELECTOR, '[title="Написать письмо"]').click()
    time.sleep(3)
    # Ввод в поле "Куда"
    email_input2 = driver.find_element(By.CSS_SELECTOR, 'input.container--H9L5q.size_s--3_M-_')
    email_input2.clear()
    email_input2.send_keys(login)
    time.sleep(1)
    # Ввод в поле "Тема письма"
    input3 = driver.find_element(By.CSS_SELECTOR, 'input[name="Subject"]')
    input3.clear()
    input3.send_keys("Тестовое письмо")
    time.sleep(1)
    # Ввод текста письма
    testletter = driver.find_element(By.CSS_SELECTOR, '.cke_editable_inline.cke_contents_true.cke_show_borders')
    testletter.clear()
    testletter.send_keys("Это тестовое письмо и бла-бла-бла")
    time.sleep(1)
    # Нажатие на кнопку прикрепить файл "Из Облака"
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.container--2lPGK.type_wide--2kyds.color_base--hO-yz.hoverable--2qtk5')
    buttons[1].click()
    time.sleep(2)
    # Выбор файла из облака
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div.b-thumb__content')
    buttons[0].click()
    buttons[2].click()
    buttons[4].click()
    time.sleep(2)
    # нажать на кнопку "прикрепить"
    button4 = driver.find_elements(By.CSS_SELECTOR, 'span[class="button2__txt"]')
    button4[1].click()
    # нажать на кнопку "отправить"
    time.sleep(3)
    button4[3].click()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()