import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('C:/Test/chromedriver.exe')
driver: WebDriver = webdriver.Chrome(service=s)
# Open site
driver.get('https://fix-online.sbis.ru/')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='wasaby-content']/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/input").send_keys("newfix")
driver.find_element(By.XPATH, "//div[@id='wasaby-content']/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/input").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='wasaby-content']/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/input").send_keys("123qwerty")
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='wasaby-content']/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/span/span").click()
time.sleep(5)
# Fill Sotrydniki
driver.get('https://fix-online.sbis.ru/page/staff-list')
time.sleep(5)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".icon-RoundPlus").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/span").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/input").send_keys("Кумпан")
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/input").send_keys("Маркиз")
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/input").send_keys("Евгеньевич")
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[4]/div[4]/span/span/i").click()
driver.find_element(By.XPATH, "//div[@id='popup']/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div[4]/div[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[4]/div[3]/div[2]/div/div/div/input").send_keys("kumpan")
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='popup']/div/div/div/div/div/div/span[2]/span/span").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='wasaby-content']/div/div/div[2]/div[3]/div/div/div/div[6]/div[2]/div[2]/div/div/div/div[2]/input").send_keys("Кумпан Маркиз Евгеньевич")
time.sleep(5)