from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


def test_remove_from_cart():
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

    # going to the cart:
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()


    # emptying the cart:
    item = driver.find_element(By.CLASS_NAME, 'cart_item')
    remove_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    time.sleep(2)
    remove_button.click()
    time.sleep(2)

    assert item.is_displayed() is False
    # assert driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').is_displayed() is False

    driver.quit()
