import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def test_add_to_basket_button(browser):
    # Load the product page for Coders at Work
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(30)

    # Find the "Add to basket" button
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Verify that the button is visible and has the correct text
    assert button.is_displayed()