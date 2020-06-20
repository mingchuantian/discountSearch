import os, time, re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class AutoCrawler:

    def __init__(self, link, basedir):
        self.link = link
        self.basedir = basedir
        self.driver = webdriver.Chrome(executable_path=os.path.join(self.basedir,'chromedriver'))

    def wait_and_click(self, classname):
        #  Sometimes click fails unreasonably. So tries to click at all cost.
        for i in range(5):
            try:
                w = WebDriverWait(self.driver, 10)
                elem = w.until(EC.presence_of_element_located((By.CLASS_NAME, classname)))
                time.sleep(4)
                elem.click()
                print("clicked")
                button_text = elem.find_element_by_class_name("text")
                print(button_text.text)
                if "NO MORE" in button_text.text:
                    print("no more products, now scrapping..")
                    break
            except:
                time.sleep(2)
                print("not clickable, loading...")
        
        


    def get_products(self):
        content = self.driver.find_element_by_id("page-content")
        products = content.find_elements_by_class_name("item")
        for product in products:
            #get brand
            brand = product.find_element_by_class_name("item-brand").text
            #get detail (description, link)
            item_detail = product.find_element_by_class_name("item-detail")
            description = item_detail.find_element_by_tag_name("a").text
            link = item_detail.find_element_by_tag_name("a").get_attribute('href')
            print(brand)
            print(description)
            print(link)

            #if there is a discounted label
            if len(product.find_elements_by_class_name("was")) > 0:
                pricewas = product.find_element_by_class_name("was").text
                pricenow = product.find_element_by_class_name("now").text
                print("Price was: "+ pricewas)
                print("Price now: "+ pricenow)
                write_csv('item-prices', [brand, description, link, pricewas, pricenow])
            #if there is no discount
            else:
                price = product.find_element_by_class_name("price-display").text
                print("Price:"+ price)
                write_csv('item-prices', [brand, description, link, price, price])
            print("------------------------------------------------------")




    def do_crawling(self):

        self.driver.get(self.link)
        self.wait_and_click("product-loader-button")
        self.get_products()
        self.driver.close()



    
