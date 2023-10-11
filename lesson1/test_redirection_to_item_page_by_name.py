from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_redirection_to_item_page_by_name():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]/div[@class="inventory_item_name"]').text

    item_name = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]/div[@class="inventory_item_name"]')
    item_name.click()

    text_after = driver.find_element(By.XPATH, '//div[text()= "Sauce Labs Fleece Jacket"]').text

    assert text_before == text_after
