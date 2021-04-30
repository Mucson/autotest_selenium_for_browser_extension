from behave import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@then('I see element with text "{text}"')
def step_impl(context, text):
    # element = (By.XPATH, "//div[@role='alertdialog']".format(text))
    element = (By.TAG_NAME, "body")
    WebDriverWait(context.driver, 10)\
        .until(ec.text_to_be_present_in_element(element, text), message="Unable to find text")
