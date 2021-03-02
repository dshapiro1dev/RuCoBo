from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Chrome(executable_path="/opt/WebDriver/bin/chromedriver")
driver = Chrome()

driver.get("https://www.onthesnow.com/united-states/skireport.html")
"""x = 0
while x < 20:
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    x += 1"""

reached_page_end = False
last_height = driver.execute_script("return document.body.scrollHeight")


while not reached_page_end:
    driver.find_element_by_xpath('//body').send_keys(Keys.END)
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        reached_page_end = True
    else:
        last_height = new_height

# elements = driver.find_elements_by_tag_name("a")
# elements = driver.find_elements_by_xpath("//a[contains(@style, 'font-size: 11px;')]")
elements =WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@style, 'font-size: 11px;')]")))

resortlinks = []
resort = {}



for item in elements:
    link = item.get_attribute("href")
    title = item.get_attribute("title")
        #if "/ski-resort.html" in link:
    if link.count("/") == 5:
        print(f"found {title} at {link}")
        resortlinks.append(link)

driver.quit()
