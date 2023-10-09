from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_all_items_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    items = driver.find_elements(By.XPATH, '//div[@class="inventory_item"]')
    for i in range(len(items)):
        product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[i].text
        add_to_cart_button = driver.find_elements(By.CLASS_NAME, "btn_inventory")[i]
        add_to_cart_button.click()
        time.sleep(2)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart.click()
    time.sleep(3)

    items_in_cart = driver.find_elements(By.XPATH, '//div[@class="cart_item"]')
    assert len(items_in_cart) == 6
    assert driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').text == "6"
