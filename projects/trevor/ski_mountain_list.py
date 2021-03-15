from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


class ski_mountain_list():
    def __init__(self):
        # Create the instance of chrome driver and load the page with all the ski mountains
        Chrome(executable_path="/opt/WebDriver/bin/chromedriver")
        self.driver = Chrome()
        self.driver.get("https://www.onthesnow.com/united-states/skireport.html")

        """The page's javascript causes only enough results to scroll down the page, and keeps loading as the 
        page scrolls. This logic will keep scrolling down, waiting 2 seconds and checking to see if anything loads
        in order to ensure the full list is loaded before parsing data. At present (3/4/21) it takes about
        22 iterations"""
        reached_page_end = False
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while not reached_page_end:
            self.driver.find_element_by_xpath('//body').send_keys(Keys.END)
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if last_height == new_height:
                reached_page_end = True
            else:
                last_height = new_height

        # Collect all href elements with the matching style of what will be links to ski resorts
        elements = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@style, 'font-size: 11px;')]")))

        self.resort_data = {}
        self.resort_data['name'] = []
        self.resort_data['link'] = []
        self.resort_count = 0

        for item in elements:
            link = item.get_attribute("href")
            title = item.get_attribute("title")
            """mixed in the links to ski resorts are links to list of resorts by state. However, these links have 4 forward
            slashes, so they can be excluded by testing for 5"""
            if link.count("/") == 5:
                print(f"found {title} at {link}")
                self.resort_count += 1
                self.resort_data['name'].append(title)
                self.resort_data['link'].append(link)

        # use panda to convert the dictionary to a dataframe and then write that to a csv
        df = pd.DataFrame(data=self.resort_data)
        self.file_name = 'resorts.csv'
        df.to_csv(self.file_name, index=False)

        # clean up by quitting the browser
        self.driver.quit()


if __name__ == "__main__":
    list = ski_mountain_list()
    print(f"found {list.resort_count} resorts which were written to file {list.file_name}")
