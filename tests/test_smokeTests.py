# Generated by Selenium IDE
import pytest
import time
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSmokeTests():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    self.driver.find_element(By.ID, "username").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("kljfas;ldkf")
    self.driver.find_element(By.ID, "password").click()
    elements = self.driver.find_elements(By.ID, "password")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "password").send_keys("dfasdlkfjasd")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".mysubmit:nth-child(4)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
    assert len(elements) > 0
  
  def test_dIrectory(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    elements = self.driver.find_elements(By.ID, "directory-grid")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.ID, "directory-list")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(5)")
    assert len(elements) > 0
  
  def test_homePage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1552, 832)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title > h1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title > h2")
    assert len(elements) > 0
    assert self.driver.title == "Teton Idaho CoC"
    elements = self.driver.find_elements(By.LINK_TEXT, "Home")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Directory")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Admin")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us").click()
    elements = self.driver.find_elements(By.ID, "content")
    assert len(elements) > 0
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("Noah")
    self.driver.find_element(By.NAME, "lname").send_keys("Ruppe")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("Creative")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Boss")
    self.driver.find_element(By.CSS_SELECTOR, "fieldset").click()
    elements = self.driver.find_elements(By.NAME, "bizname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".join-wizard-main")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "email").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
