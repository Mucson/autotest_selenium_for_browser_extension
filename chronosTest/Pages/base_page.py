from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        # expected_condition_q = ec.
        expected_conditions = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 15).until(expected_conditions, message="Something went wrong")

    def click_on(self, locator):
        self.get_element(locator).click()

    def type_in(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text
