from chronosTest.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    GetStartedButton = (By.XPATH, "//*[text()=' Get Started ']")
    ImportAccountButton = (By.XPATH, "//*[text()=' Import Account ']")
    CreateAccountButton = (By.XPATH, "//*[text()=' Create Account ']")
    SeedPhraseField = (By.XPATH, "//input[@name='seedPhrase']")
    PasswordField = (By.XPATH, "//input[@name='password']")
    ConfirmPasswordField = (By.XPATH, "//input[@name='confirmPassword']")
    ImportAccount = (By.XPATH, "//*[text()=' IMPORT ']")
    SmallMenuOpenButton = (By.XPATH, "//div[contains(@class, 'mat-menu-trigger')]")
    LockAccountButton = (By.XPATH, "//*[text()='Lock account']")
    UnlockAccountButton = (By.XPATH, "//*[text()=' UNLOCK ']")
    InitRestoreAccountButton = (By.XPATH, "//a[text()='Restore Your Account']")
    ConfirmRestoreAccountButton = (By.XPATH, "//*[text()=' RESTORE ']")

    def click_on_get_started_button(self):
        self.click_on(self.GetStartedButton)

    def click_on_import_account_button(self):
        self.click_on(self.ImportAccountButton)

    # def click_on_create_account_button(self):
    #     self.click_on(self.CreateAccountButton)
    #     self.driver.find_element_by_xpath("//*[text()=' Create an Account ']").click()

    def enter_seed_phrase(self, text):
        self.type_in(self.SeedPhraseField, text)

    def enter_password(self, password):
        self.type_in(self.PasswordField, password)

    def enter_confirm_password(self, password):
        self.type_in(self.ConfirmPasswordField, password)

    def click_on_import_account(self):
        self.click_on(self.ImportAccount)

    def open_small_menu(self):
        self.click_on(self.SmallMenuOpenButton)

    def lock_account(self):
        self.click_on(self.LockAccountButton)

    def unlock_account(self):
        self.click_on(self.UnlockAccountButton)

    def restore_account_init(self):
        self.click_on(self.InitRestoreAccountButton)

    def restore_account(self):
        self.click_on(self.ConfirmRestoreAccountButton)
