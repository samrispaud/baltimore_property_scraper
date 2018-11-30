from driver import Driver
from html_parser import Parser
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, driver, street_number, street_name):
        # Go to SDAT property search website
        driver.navigate_to_website("http://sdat.dat.maryland.gov/RealProperty/Pages/default.aspx")

        # counties include BALTIMORE CITY, BALTIMORE COUNTY, etc
        driver.select_search_param("BALTIMORE CITY")

        # find property
        driver.search_property(street_number, street_name)

        # scrape html
        html_string = driver.page_source
        parser = Parser(html_string)

        # hash for finding data
        ids_to_search = {
                'owner_name': 'lblOwnerName_0',
                'use': 'lblUse_0',
                'principal_residence': 'lblPrinResidence_0',
                'mailing_address': 'lblMailingAddress_0',
                'deed_reference': 'lblDedRef_0',
                'premises_address': 'lblPremisesAddress_0',
                'legal_description': 'lblLegalDescription_0',
                'primary_structure_built': 'Label18_0',
                'above_grade_living_area': 'Label19_0',
                'finished_basement_area': 'Label27_0',
                'property_land_area': 'Label20_0',
                'stories': 'Label22_0',
                'basement': 'Label23_0',
                'bldg_type': 'Label24_0',
                'exterior': 'Label25_0',
                'full_half_bath': 'Label34_0',
                'garage': 'Label35_0',
                'last_major_reno': 'Label36_0',
                'last_deed_transfer_seller': 'Label38_0',
                'last_deed_transfer_date': 'Label39_0',
                'last_deed_transfer_price': 'Label40_0',
                'last_deed_transfer_type': 'Label41_0'
            }

        data_dict = {}

        for key, val in ids_to_search.items():
            data = parser.strip_data_from_html(val)
            data_dict[key] = data

        self.property_data = data_dict
