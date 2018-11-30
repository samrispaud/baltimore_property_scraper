from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

class Driver:
    def __init__(self, file_path):
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=file_path, chrome_options=options)
        driver.wait = WebDriverWait(driver, 10)
        self.driver = driver
        self.options = options

    def navigate_to_website(self, site):
        self.driver.get(site)

    def select_search_param(self, county):
        county_css_id = "MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchType_ddlCounty"
        search_method = "MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchType_ddlSearchType"

        select = Select(self.driver.find_element_by_id(county_css_id))
        select.select_by_visible_text(county)

        select = Select(self.driver.find_element_by_id(search_method))
        select.select_by_visible_text("STREET ADDRESS")
        time.sleep(1)

        click_continue_id = "MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_StartNavigationTemplateContainerID_btnContinue"
        self.driver.find_element_by_id(click_continue_id).click()
        time.sleep(1)

    def search_property(self, street_number, street_name):
        street_number_input_id = "MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreenNumber"
        street_name_input_id = "MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreetName"

        self.driver.find_element_by_id(street_number_input_id).send_keys(street_number)
        self.driver.find_element_by_id(street_name_input_id).send_keys(street_name)
        time.sleep(1)

        click_continue_id = "MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_StepNavigationTemplateContainerID_btnStepNextButton"
        self.driver.find_element_by_id(click_continue_id).click()
        time.sleep(2)
        try:
            # if north and south street exists for a given number need to pick south one
            south_street_query = "//*[contains(text(), '" + street_name.upper() + " S ')][1]/parent::*[1]/preceding-sibling::*"
            self.driver.find_elements_by_xpath(south_street_query)[0].click()
            time.sleep(2)
            self.page_source = self.driver.page_source
        except:
            self.page_source = self.driver.page_source

    def close_connection(self):
        self.driver.quit()
