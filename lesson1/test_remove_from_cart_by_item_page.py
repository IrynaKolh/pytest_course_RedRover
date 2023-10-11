from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


def test_remove_from_cart_by_item_page():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # adding item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()
    time.sleep(1)

    # going to the item page:
    item_name = driver.find_element(By.XPATH, '//*[text() = "Sauce Labs Backpack"]')
    item_name.click()

    # click the remove btn:
    remove_from_cart_button = driver.find_element(By.XPATH, '//button[@data-test ="remove-sauce-labs-backpack"]')
    remove_from_cart_button.click()
    time.sleep(1)

    # going to the cart:
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()

    assert not driver.find_elements(By.XPATH, '//div[@class="cart_item"]')

    driver.quit()
