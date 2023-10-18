from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

from LearnPytest.test_LearnSelenium import LearnSelenium


class TestChildLocator:
    def test_method(self):
        driver = webdriver.Chrome()
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[@class='_30XB9F']").click()
        time.sleep(3)
        coding = LearnSelenium(driver)
        coding.get_all_child_menu_items_name()
        coding.close_Browser()
