from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class UserPage(BasePage):
    EditProfileButton = (By.XPATH, "//*[text()='Edit account information']/..")
    SmallMenuOpenButton = (By.XPATH, "//div[contains(@class, 'menu__trigger')]")
    dPortalPageButton = (By.XPATH, "//div[@data-id='dportal']")

    def edit_profile(self):
        self.click_on(self.EditProfileButton)

    def open_small_menu(self):
        self.click_on(self.SmallMenuOpenButton)

    def open_dportal_page(self):
        self.click_on(self.dPortalPageButton)
