import os
from app import crawler
#from crawler import AutoCrawler
from app.write_csv import create_csv
from app.crawler import AutoCrawler
from app import Config
    
class Sites:

    '''
    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
    '''

    def run_crawler(self):
        
        with open("websites.txt", 'r') as websites:
            create_csv('item-prices', ['Brand', 'Description', 'link', 'pricewas', 'pricenow'])
            for site in websites:
                autocrawler = AutoCrawler(site, Config.basedir)
                autocrawler.do_crawling()
        

sites = Sites()
sites.run_crawler()
