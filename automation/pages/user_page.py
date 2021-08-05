from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class UserPage(BasePage):
    SmallMenuOpenButton = (By.XPATH, "//div[contains(@class, 'menu__trigger')]")
    EditProfileButton = (By.XPATH, "//*[text()='Edit account information']/..")
    SettingsButton = (By.XPATH, "//*[text()='Settings']")
    LockAccountButton = (By.XPATH, "//*[text()='Lock account']")
    DeleteAccountButton = (By.XPATH, "//*[text()='Delete account']")
    dPortalPageButton = (By.XPATH, "//div[@data-id='dportal']")

    def _verify_page_(self):
        self.on_this_page(self.SmallMenuOpenButton, self.EditProfileButton, self.SettingsButton,
                          self.LockAccountButton, self.DeleteAccountButton)

    def edit_profile(self):
        self.click_on(self.EditProfileButton)

    def open_small_menu(self):
        self.click_on(self.SmallMenuOpenButton)

    def open_dportal_page(self):
        self.click_on(self.dPortalPageButton)
