from behave import *
from models.get_attr_from_dict import GetAttrFromDict
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.elements_page import ElementsPage

@given("Go to Demo page")
def navigate_to_demo(context):
    context.base_page = BasePage(context.driver)
    context.base_page.navigate_to_url(context.env_data["url"])

@when("Select {name} option")
def select_option(context, name: str):
    context.home_page = HomePage(context.driver)
    context.selected_option = name
    context.option_attributes = GetAttrFromDict(context.env_data[context.selected_option])
    context.home_page.select_module_option(context.option_attributes)

@when("Select {module} module")
def select_module(context, module: str):
    context.selected_module = module
    context.module_attributes = GetAttrFromDict(context.env_data[context.selected_option]["modules"][context.selected_module])
    context.elements_page = ElementsPage(context.driver)
    context.elements_page.select_element_module(context.module_attributes.text)

@when("Enter {data} to textbox")
def enter_textbox_data(context, data: str):
    context.data_attributes = GetAttrFromDict(context.env_data[context.selected_option]["modules"][context.selected_module][data])
    context.elements_page.enter_data_to_textbox(context.data_attributes)