from selenium.webdriver import Chrome
import time
Chrome(executable_path="/opt/WebDriver/bin/chromedriver")
driver = Chrome()



driver.get("https://www.onthesnow.com/new-england/skireport.html")
time.sleep(5)
elements = driver.find_elements_by_tag_name("a")

resortlinks = []
resort = {}

for item in elements:
    link = item.get_attribute("href")
    title = item.get_attribute("title")
    try:
        if "/ski-resort.html" in link:
            print(f"found {title} at {link}")
            resortlinks.append(link)
    except (TypeError):
        continue


# driver.quit()