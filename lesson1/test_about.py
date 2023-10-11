from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_about():
    driver.get("https://www.saucedemo.com/")
    before_url = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(3)

    logout = driver.find_element(By.ID, 'about_sidebar_link')
    logout.click()
    time.sleep(1)

    after_url = driver.current_url

    assert after_url != before_url
    assert after_url == 'https://saucelabs.com/'

    driver.quit()
