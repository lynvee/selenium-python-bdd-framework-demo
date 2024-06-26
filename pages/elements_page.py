from selenium.webdriver.common.by import By
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage
from utils.custom_webdriver import CustomWebDriver

class ElementsPage(BasePage):

    def __init__(self, driver: CustomWebDriver) -> None:
        super().__init__(driver)
    
    # LOCATORS:
    # Text Box
    FULLNAME_TEXTBOX = (By.XPATH, "//input[@id='userName']")
    EMAIL_TEXTBOX = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS_TEXTBOX = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS_TEXTBOX = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    # Check Box
    # Radio Button
    YES_RADIO = (By.XPATH, "//input[@id='yesRadio']")
    IMPRESSIVE_RADIO = (By.XPATH, "//input[@id='impressiveRadio']")
    CONFIRM_OPTION = (By.XPATH, "//span[@class='text-success']")

    # ACTIONS:
    def select_element_module(self, modulename: str):
        element_module = (By.XPATH, f"//span[contains(text(), '{modulename}')]")
        self.driver.click_element(*element_module)
    # Text Box
    def enter_data_to_textbox(self, info: GetAttrFromDict):
        self.type_text(*self.FULLNAME_TEXTBOX, info.fullname)
        self.type_text(*self.EMAIL_TEXTBOX, info.email)
        self.type_text(*self.CURRENT_ADDRESS_TEXTBOX, info.currentaddress)
        self.type_text(*self.PERMANENT_ADDRESS_TEXTBOX, info.permanentaddress)
    
    def textbox_submit(self):
        self.driver.click_element(*self.SUBMIT_BUTTON)
    # Radio Button
    