import urllib3.request
from selenium import webdriver

# def page_loaded(self):
#     self.log.info("checking if {} page is loaded.".format(self.driver.current_url))
#     try:
#         new_page = browser.find_element_by_tag_name('html')
#         return new_page.id != old_page.id
#     except NoSuchElementException:
#         return False
#driver = webdriver.Firefox(executable_path='C:/Program Files/geckodriver.exe')
driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')
driver.get('https://www.flipkart.com/oppo-a9-2020-marine-green-128-gb/p/itm32799ab1d45b4?pid=MOBFKCS5G9MSXBVF&lid=LSTMOBFKCS5G9MSXBVF83WPUP&otracker=clp_banner_1_8.bannerX3.BANNER_mobiles-big-saving-days-ko7y7ui3-store_VAUZJXIDPAKJ&fm=neo%2Fmerchandising&iid=M_603ac043-370c-40f1-a3d5-4e6bdaabc922_8.VAUZJXIDPAKJ&ssid=3dxp01s5800000001593015914018')
#button = driver.find_element_by_xpath('//button[contains(text(), "test button")]')
button = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
driver.maximize_window()
#print(len(button))
driver.execute_script("window.scrollTo(0, 4500)") 
# from selenium.webdriver.support.wait import WebDriverWait
# element = WebDriverWait(driver, 7).until(
#     lambda x: x.find_element_by_xpath('//[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/button'))

#button = driver.find_element_by_xpath('//[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
print("loaded")
button.click()
# for i in button:
#     i.click()

# while True:
#     if page_loaded(driver):    
#         print("page loaded")
#         for i in button:
#             i.click()
#         break

print('done')
# weburl = urllib.request.urlopen("https://theopensourceworld.com")
# #print("result code:", weburl.getcode())
# html = weburl.read()
# with open('page.html', 'wb') as f:
#     f.write(html)
# print("done")