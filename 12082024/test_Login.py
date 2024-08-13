import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@allure.title("Verify login to the katalon-demo-cura.herokuapp.com")
@allure.description("Verify login to the katalon-demo-cura.herokuapp.com is successful")
def test_Login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_appointment = driver.find_element(By.ID, value='btn-make-appointment')
    make_appointment.click()
    time.sleep(2)
    # Assert that the actual title is equal to the expected title
    actual_title = driver.title
    # print(actual_title)
    expected_title = "CURA Healthcare Service"
    assert actual_title == expected_title, "Title match"
    # time.sleep(10)
    user_name = driver.find_element(By.ID, value='txt-username')
    user_name.send_keys('John Doe')
    pass_word = driver.find_element(By.ID, value='txt-password')
    pass_word.send_keys('ThisIsNotAPassword')
    login_button = driver.find_element(By.ID, value='btn-login')
    login_button.click()
    visible_txt = driver.find_element(By.XPATH, value='//*[@id="appointment"]/div/div/div/h2').text
    print(visible_txt)
    assert visible_txt == 'Make Appointment', "Text visible"
    time.sleep(10)
    driver.quit()
