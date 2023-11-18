# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestProject2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_project2(self):
    self.driver.get("https://www.gov.hk/tc/residents/")
    self.driver.set_window_size(812, 518)
    self.driver.find_element(By.CSS_SELECTOR, ".myGov").click()
    assert self.driver.find_element(By.ID, "ws-mygovhk-register").text == "登記"
    assert self.driver.title == "GovHK 香港政府一站通：本港居民(主頁)"
    self.driver.find_element(By.ID, "tabBizTrade").click()
    assert self.driver.find_element(By.LINK_TEXT, "公司稅務").text == "公司稅"
    self.driver.find_element(By.ID, "tabNonResidents").click()
    assert self.driver.find_element(By.LINK_TEXT, "非香港居民薪俸稅").text == "非香港居民薪俸稅"
    self.driver.find_element(By.ID, "tabResidents").click()
    self.driver.find_element(By.ID, "ws-desktop-lang-other").click()
    self.driver.find_element(By.ID, "ws-desktop-lang-en").click()
    self.driver.find_element(By.CSS_SELECTOR, ".myGov").click()
    assert self.driver.find_element(By.ID, "ws-mygovhk-register").text == "Register"
    assert self.driver.title == "GovHK: Residents (Homepage)"
    self.driver.find_element(By.ID, "tabBizTrade").click()
    assert self.driver.find_element(By.LINK_TEXT, "Corporate Tax").text == "Corporate Tax"
    self.driver.find_element(By.ID, "tabNonResidents").click()
    assert self.driver.find_element(By.LINK_TEXT, "Non-Residents Salaries Tax").text == "Non-Residents Salaries Tax"
    self.driver.find_element(By.ID, "tabResidents").click()
    self.driver.find_element(By.ID, "ws-desktop-lang-other").click()
    self.driver.find_element(By.ID, "ws-desktop-lang-sc").click()
    self.driver.find_element(By.CSS_SELECTOR, ".myGov").click()
    assert self.driver.find_element(By.ID, "ws-mygovhk-register").text == "登记"
    assert self.driver.title == "GovHK 香港政府一站通：本港居民(主页)"
    self.driver.find_element(By.ID, "tabBizTrade").click()
    assert self.driver.find_element(By.LINK_TEXT, "公司税务").text == "公司税务"
    self.driver.find_element(By.ID, "tabNonResidents").click()
    assert self.driver.find_element(By.LINK_TEXT, "非香港居民薪俸税").text == "非香港居民薪俸税"
    self.driver.find_element(By.ID, "tabResidents").click()
    self.driver.find_element(By.ID, "ws-desktop-lang-other").click()
    self.driver.find_element(By.ID, "ws-desktop-lang-tc").click()
  
