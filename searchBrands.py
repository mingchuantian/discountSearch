import os, time
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
#import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
basedir = os.path.abspath(os.path.dirname(__file__))
driver = webdriver.Chrome(executable_path=os.path.join(basedir,'chromedriver'))
driver.get('https://www.davidjones.com/brand/apple')

#loadPage = ActionChains(driver)

try:
    loaderButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-loader-button"))
    )
finally:
    print(loaderButton.text)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollBy(0, -50)")
    time.sleep(5)
    loaderButton.click()
    time.sleep(5)
    
    

driver.quit()
'''
try:
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-content"))
    )
    

    products = content.find_elements_by_class_name("item")

    for product in products:
        #there is a discounted label
        if len(product.find_elements_by_class_name("was")) > 0:
            pricewas = product.find_element_by_class_name("was")
            pricenow = product.find_element_by_class_name("now")
            item_detail = product.find_element_by_class_name("item-detail")
            brand = item_detail.find_element_by_class_name("item-brand")
            description = item_detail.find_element_by_tag_name("a")
            link = description.get_attribute('href')
            print(brand.text)
            print(description.text)
            print(link)
            print("price was")
            print(pricewas.text) 
            old_price = int(float(pricewas.text[1:].replace(',','')))
            print("price now")
            print(pricenow.text) 
            new_price = int(float(pricenow.text[1:].replace(',','')))
            print("discount rate")
            print(new_price/old_price)

            print("-------------------------------")

        #else:
            #price = product.find_element_by_class_name("item-brand")
            #print(price.text)
            

finally:
    driver.quit()
'''