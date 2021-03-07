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

        """Get the terrain details with a varying number of components on the page
        The terrains section includes count of runs, area, and types of trails. But not
        all the sections are consistently used. The code below will grab the full list and
        turn it inot an array. We will then talk through the array where a value is identified
        by te prior value"""
        terrain_text = driver.find_element_by_xpath("//ul[contains(@class, 'rt_trail diamonds')]").text
        terrain_list = terrain_text.splitlines()
        linenumber = 0

        runs = 0
        pct_beginner = 0
        pct_intermediate = 0
        pct_advanced = 0
        pct_expert = 0

        for line in terrain_list:
            if line == 'RUNS':
                runs = float(terrain_list[linenumber + 1])
                self.details["runs"] = terrain_list[linenumber + 1]
            if line == 'BEGINNER RUNS':
                pct_beginner = p2f(terrain_list[linenumber + 1])
                self.details["pct beginner"] = pct_beginner
            if line == 'INTERMEDIATE RUNS':
                pct_intermediate = p2f(terrain_list[linenumber + 1])
                self.details["pct intermediate"] = pct_intermediate
            if line == 'ADVANCED RUNS':
                pct_advanced = p2f(terrain_list[linenumber + 1])
                self.details["pct advanced runs"] = pct_advanced
            if line == 'EXPERT RUNS':
                pct_expert = p2f(terrain_list[linenumber + 1])
                self.details["pct expert runs"] = pct_expert
            linenumber += 1

        # Set number for any percent

        if pct_beginner > 0:
            self.details['beginner runs'] = round(runs * pct_beginner)
        else:
            self.details['beginner runs'] = 0

        if pct_intermediate > 0:
            self.details['intermediate runs'] = round(runs * pct_intermediate)
        else:
            self.details['intermediate runs'] = 0

        if pct_advanced > 0:
            self.details['advanced runs'] = round(runs * pct_advanced)
        else:
            self.details['advanced runs'] = 0

        if pct_expert > 0:
            self.details['expert runs'] = round(runs * pct_expert)
        else:
            self.details['expert runs'] = 0

        driver.quit()


def p2f(x):
    if x == "%":
        return 0
    else:
        return float(x.strip('%')) / 100


if __name__ == "__main__":
    mountain = ski_mountain("https://www.onthesnow.com/vermont/killington-resort/ski-resort.html")
    print(mountain.details)
