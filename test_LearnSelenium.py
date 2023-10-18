from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver


class LearnSelenium :
    driver=""
    parent_menu_items = "//div[@class='_3sdu8W emupdz']"
    child_menu_items_name1 = ".//div[@class='_1ch8e_']"
    child_menu_items_name2 = "//a[@class='_1ch8e_']"

    def __init__(self,driver):
        self.driver = driver

    def get_all_child_menu_items_name(self):
        menu_items= self.driver.find_elements(By.XPATH,self.parent_menu_items)
        print("menu items name are :----------")
        for menu in menu_items:
            print(menu.find_element(By.XPATH,self.child_menu_items_name1).text)

        for menu2 in menu_items:
            print(menu2.find_element(By.XPATH,self.child_menu_items_name2).text)

    def close_Browser(self):
        self.driver.close()

