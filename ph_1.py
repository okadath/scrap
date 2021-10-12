from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")
base_url = "https://twitter.com"

def login(driver):
	print("logeando")
	driver.get(base_url)
	time.sleep(1)
	username = driver.find_element_by_name("session[username_or_email]")
	password = driver.find_element_by_name("session[password]")
	time.sleep(1)
	username.send_keys("bototuit@mail.com")
	password.send_keys("Qwerty35$")
	time.sleep(1)
	elem = driver.find_element_by_xpath("//input[@class='EdgeButton EdgeButton--secondary EdgeButton--medium submit js-submit'][@type='submit']")
	elem.click()

try:
	print("1")
	driver=webdriver.PhantomJS(service_args=["--load-images=no"])# or add to your PATH
	# f_profile = webdriver.FirefoxProfile()
	# #firefox_profile.set_preference('permissions.default.stylesheet', 2)
	# f_profile.set_preference('permissions.default.image',2)
	# driver = webdriver.Firefox(firefox_profile=f_profile)
	print("2")
	driver.set_window_size(1024, 768) # optional
	# driver.get('https://google.com/')
	login(driver)
	driver.save_screenshot('capturas/screen.png')
	
except Exception as e:
	print("error:",e)
finally:
	print("termino")
	#driver.quit()


	from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options as GoogleOptions


# # driver_nav="google"
# driver_nav="firefox"
# headless=False

# def init_client():
# 		# print("1")
# 	try:
# 		if driver_nav=="google":
# 			chrome_options = GoogleOptions()
# 			#chrome_options.add_argument("--disable-extensions")
# 			#chrome_options.add_argument("--disable-gpu")
# 			#chrome_options.add_argument("--no-sandbox") # linux only
# 			if headless:
# 				chrome_options.add_argument("--headless")
# 			# chrome_options.headless = True # also works
# 			driver = webdriver.Chrome(options=chrome_options)

# 		if driver_nav=="firefox":
# 			# driver=webdriver.PhantomJS(service_args=["--load-images=no"])# or add to your PATH
# 			f_profile = webdriver.FirefoxProfile()
# 			# #firefox_profile.set_preference('permissions.default.stylesheet', 2)
# 			# f_profile.set_preference('permissions.default.image',2)
# 			options = FirefoxOptions()
# 			if headless:
# 				options.headless = True
# 			driver = webdriver.Firefox(firefox_profile=f_profile, firefox_options=options)
# 			# print("2")
# 		driver.set_window_size(1024, 768) # optional
# 		# driver.get('https://google.com/')	
# 		return driver
# 	except Exception as e:
# 		raise e
# 		return 0

# # dcap = dict(DesiredCapabilities.PHANTOMJS)
# # dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")
# # base_url = "https://twitter.com"

# # def login(driver):
# # 	print("logeando")
# # 	driver.get(base_url)
# # 	time.sleep(1)
# # 	username = driver.find_element_by_name("session[username_or_email]")
# # 	password = driver.find_element_by_name("session[password]")
# # 	time.sleep(1)
# # 	username.send_keys("bototuit@mail.com")
# # 	password.send_keys("Qwerty35$")
# # 	time.sleep(1)
# # 	elem = driver.find_element_by_xpath("//input[@class='EdgeButton EdgeButton--secondary EdgeButton--medium submit js-submit'][@type='submit']")
# # 	elem.click()

# # try:
# # 	print("1")
# # 	# driver=webdriver.PhantomJS(service_args=["--load-images=no"])# or add to your PATH
# # 	f_profile = webdriver.FirefoxProfile()
# # 	# #firefox_profile.set_preference('permissions.default.stylesheet', 2)
# # 	# f_profile.set_preference('permissions.default.image',2)
# # 	driver = webdriver.Firefox(firefox_profile=f_profile)
# # 	print("2")
# # 	driver.set_window_size(1024, 768) # optional
# # 	# driver.get('https://google.com/')
# # 	login(driver)
# # 	driver.save_screenshot('capturas/screen.png')
	
# # except Exception as e:
# # 	print("error:",e)
# # finally:
# # 	print("termino")

# driver=init_client()
# driver.get("https://www.duckduckgo.com")


# # from selenium import webdriver 
# # from selenium.webdriver.chrome.options import Options
# # chrome_options = Options()
# # #chrome_options.add_argument("--disable-extensions")
# # #chrome_options.add_argument("--disable-gpu")
# # #chrome_options.add_argument("--no-sandbox") # linux only
# # # ~ chrome_options.add_argument("--headless")
# # # chrome_options.headless = True # also works
# # driver = webdriver.Chrome(options=chrome_options)
# # start_url = "https://duckgo.com"
# # driver.get(start_url)
# # print(driver.page_source.encode("utf-8"))
# # driver.quit()
