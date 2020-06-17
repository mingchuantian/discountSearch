from selenium.webdriver.chrome.options import Options

#option for headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=os.path.join(basedir,'chromedriver'), chrome_options=chrome_options)