import os
from crawler import AutoCrawler
    
class Sites:

    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def run_crawler(self):
        with open("websites.txt") as websites:
            for site in websites:
                autocrawler = AutoCrawler(site, self.basedir)
                autocrawler.do_crawling()
                break

sites = Sites()
sites.run_crawler()
