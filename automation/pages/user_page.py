from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class UserPage(BasePage):
    EditProfileButton = (By.XPATH, "//*[text()='Edit account information']/..")

    def edit_profile(self):
        self.click_on(self.EditProfileButton)
