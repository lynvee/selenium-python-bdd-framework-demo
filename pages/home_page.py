from selenium.webdriver.common.by import By
from utils.custom_webdriver import CustomWebDriver
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage
from pages.elements_page import ElementsPage

class HomePage(BasePage):

    def __init__(self, driver: CustomWebDriver) -> None:
        super().__init__(driver)
    
    # LOCATORS:

    # ACTIONS:
    def select_module_option(self, module: GetAttrFromDict):
        option_locator = (By.XPATH, f"//h5[contains(text(), '{module.title}')]")
        self.driver.click_element(*option_locator)
        self.driver.wait_for_url_match(module.expected_url)