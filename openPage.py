import os, time
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
basedir = os.path.abspath(os.path.dirname(__file__))

'''driver = webdriver.Chrome('./chromedriver')'''

driver = None
driver = webdriver.Firefox(executable_path=os.path.join(basedir,'geckodriver'))
driver.get('https://www.davidjones.com/')


time.sleep(5) 
search_field = driver.find_element_by_id('searchterm')

search_field.send_keys('a')
search_field.send_keys(Keys.ENTER)

load = driver.find_element_by_xpath("//*[contains(text(), 'Load')]")

time.sleep(5)
load.click()

'''
wait = WebDriverWait(driver, 5)

wait.until(expected_conditions.visibility_of(load))
load.click()
'''

'''
driver.find_element_by_xpath('//button[text()="Load next 90 styles"]').click()
while driver.find_element_by_xpath('//button[text()="Load next 90 styles"]'):
    driver.find_element_by_xpath('//button[text()="Load next 90 styles"]').click()
    time.sleep(1)
'''

