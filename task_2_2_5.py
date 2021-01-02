from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)
    button2 = browser.find_element_by_css_selector("button[type=submit]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
