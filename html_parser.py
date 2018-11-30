#
# owner_name = 'lblOwnerName_0'
# use = 'lblUse_0'
# principal_residence = 'lblPrinResidence_0'
# mailing_address ='lblMailingAddress_0'
# deed_reference = 'lblDedRef_0'
# premises_address = 'lblPremisesAddress_0'
# legal_description = 'lblLegalDescription_0'
# primary_structure_built = 'Label18_0'
# above_grade_living_area = 'Label19_0'
# finished_basement_area = 'Label27_0'
# property_land_area = 'Label20_0'
# stories = 'Label22_0'
# basement = 'Label23_0'
# type_xpath = 'Label24_0'
# exterior = 'Label25_0'
# full_half_bath = 'Label34_0'
# garage = 'Label35_0'
# last_major_reno = 'Label36_0'
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html):
        self.soup_obj = BeautifulSoup(html, "lxml")

    def strip_data_from_html(self, element_id):
        base_id_string = 'MainContent_MainContent_cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucDetailsSearch_dlstDetaisSearch_'

        try:
            data = self.soup_obj.find(
                "span", {"id" : base_id_string + element_id}).get_text().strip()
        except (ValueError, AttributeError):
            data = None
        if len(data) == 0:
            data = None
        return(data)
