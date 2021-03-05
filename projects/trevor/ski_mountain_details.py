from selenium.webdriver import Chrome
import time
# Chrome(executable_path="/opt/WebDriver/bin/chromedriver")

class ski_mountain():

    def __init__(self, url):
        driver = Chrome()
        self.name = ""
        self.details = {}

        # try to go through one mountain and collect information
        driver.get(url)
        time.sleep(3)

        # Get the resort Name
        resort_name = driver.find_element_by_xpath("//span[contains(@class, 'resort_name')]").text
        self.name = resort_name

        # Get the longest run
        # longest_run = driver.find_element_by_xpath("//ul[contains(@class, 'rt_trail diamonds')]/li[8]/p[2]").text
        # self.details["longest_run"] = longest_run

        # Get the Max elevation
        resort_summit = driver.find_element_by_xpath("//li[contains(@class, 'top')]/div[1]").text
        self.details["summit"] = resort_summit

        # Get the Drop in elevation
        resort_drop = driver.find_element_by_xpath("//li[contains(@class, 'drop')]/div[1]").text
        self.details["drop"] = resort_drop

        # Get the lift info
        resort_trams = driver.find_element_by_xpath("//li[contains(@class, 'trams')]").text
        self.details["trams"] = resort_trams

        driver.quit()

if __name__ == "__main__":
    mountain = ski_mountain("https://www.onthesnow.com/vermont/killington-resort/ski-resort.html")
    print(mountain.details)
