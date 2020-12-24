import re
import time
import requests
from selenium import webdriver
from lxml.html import fromstring
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("location_to/chromedriver.exe")
bs_driver = webdriver.Chrome("location_to/chromedriver.exe")

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target = '"Carlo 7"'
x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
patience = 10

bs_driver.get("https://sebpearce.com/bullshit/")
bs_xpath = '/html/body/div[7]/button'
bs_xpath_title = '//*[@id="main-heading"]'

for i in range(patience):
    bs_driver.find_element_by_xpath(bs_xpath_reroll).click()
    string = bs_driver.find_element_by_xpath(bs_xpath_title).text
    input_box.send_keys(string.format(i) + Keys.ENTER)
    time.sleep(10)
