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

        for i in range(20):
            try:
                w = WebDriverWait(self.driver, 10)
                elem = w.until(EC.presence_of_element_located((By.CLASS_NAME, classname)))
                time.sleep(4)
                elem.click()
                print("clicked")
                button_text = elem.find_element_by_class_name("text")
                print(button_text.text)
                if "NO MORE" in button_text.text:
                    break
            except:
                time.sleep(2)
                print("not clickable, loading...")
        self.get_products()

    def get_products(self):
        print("now get products")
        content = self.driver.find_element_by_id("page-content")
        products = content.find_elements_by_class_name("item")
        for product in products:
            #there is a discounted label
            if len(product.find_elements_by_class_name("was")) > 0:
                pricewas = product.find_element_by_class_name("was").text
                pricenow = product.find_element_by_class_name("now").text

                brand = product.find_element_by_class_name("item-brand").text

                item_detail = product.find_element_by_class_name("item-detail")
                brand = item_detail.find_element_by_class_name("item-brand").text

                description = item_detail.find_element_by_tag_name("a")
                link = description.get_attribute('href')
                

                print(brand)
                print(description.text)
                print(link)

                price_was = int(re.findall(r'\d+', pricewas)[0])
                print("price was: AU$" + str(price_was)) 
                price_now = int(re.findall(r'\d+', pricenow)[0])
                print("price now: AU$" + str(price_now)) 

                print("discount rate: " + str(price_now/price_was))
                print("-------------------------------")


    def do_crawling(self):

        self.driver.get(self.link)
        self.wait_and_click("product-loader-button")



    
