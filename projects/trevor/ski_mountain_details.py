from selenium.webdriver import Chrome
import time
# Chrome(executable_path="/opt/WebDriver/bin/chromedriver")
driver = Chrome()

resort_info = {}

# try to go through one mountain and collect information
driver.get("https://www.onthesnow.com/north-carolina/sugar-mountain-resort/ski-resort.html")
time.sleep(3)

# Get the resort Name
resort_name = driver.find_element_by_xpath("//span[contains(@class, 'resort_name')]").text
resort_info["name"] = resort_name

# Get the Max elevation
resort_summit = driver.find_element_by_xpath("//li[contains(@class, 'top')]/div[1]").text
resort_info["summit"] = resort_summit

# Get the lift info
resort_trams = driver.find_element_by_xpath("//li[contains(@class, 'trams')]").text
resort_info["trams"] = resort_trams

print(resort_info)

driver.quit()