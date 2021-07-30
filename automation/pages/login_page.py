from automation.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    WelcomeMessageTitle = (By.XPATH, "//div[@class='page-title']")
    GetStartedButton = (By.XPATH, "//*[text()=' Get Started ']")
    ImportAccountButton = (By.XPATH, "//*[text()=' Import Account ']")
    CreateAccountButton = (By.XPATH, "//*[text()=' Create Account ']")
    SeedPhraseField = (By.XPATH, "//input[@name='seedPhrase']")
    PasswordField = (By.XPATH, "//input[@name='password']")
    ConfirmPasswordField = (By.XPATH, "//input[@name='confirmPassword']")
    ImportAccount = (By.XPATH, "//*[text()=' IMPORT ']")
    LockAccountButton = (By.XPATH, "//div[@data-id='lock account']")
    UnlockAccountButton = (By.XPATH, "//*[text()=' UNLOCK ']")
    InitRestoreAccountButton = (By.XPATH, "//a[text()='Restore Your Account']")
    ConfirmRestoreAccountButton = (By.XPATH, "//*[text()=' RESTORE ']")
    BackButton = (By.XPATH, "//div[contains(@class, 'btn__back')]")
    LetsDecentrPageTitle = (By.XPATH, "//div[@class='page-title']")
    LetsDecentrPageSubTitle = (By.XPATH, "//div[@class='page-subtitle']")
    RestoreAccountPageTitle = (By.XPATH, "//div[contains(@class, 'page-title')]")
    RestoreAccountPageContent = (By.XPATH, "//div[@class='page-content']")
    ConfirmCookieButton = (By.XPATH, "//button[@type='button']")
    AllDoneButton = (By.XPATH, "//*[text()=' ALL DONE ']")

    def get_welcome_message_title(self):
        return self.get_text(self.WelcomeMessageTitle)

    def click_on_get_started_button(self):
        self.click_on(self.GetStartedButton)

    def click_on_import_account_button(self):
        self.click_on(self.ImportAccountButton)

    def enter_seed_phrase(self, text):
        self.type_in(self.SeedPhraseField, text)

    def enter_password(self, password):
        self.type_in(self.PasswordField, password)

    def enter_confirm_password(self, password):
        self.type_in(self.ConfirmPasswordField, password)

    def click_on_import_account(self):
        self.click_on(self.ImportAccount)

    def lock_account(self):
        self.click_on(self.LockAccountButton)

    def unlock_account(self):
        self.click_on(self.UnlockAccountButton)

    def restore_account_init(self):
        self.click_on(self.InitRestoreAccountButton)

    def restore_account(self):
        self.click_on(self.ConfirmRestoreAccountButton)

    def click_back_button(self):
        self.click_on(self.BackButton)

    def get_lets_decentr_page_title(self):
        return self.get_text(self.LetsDecentrPageTitle)

    def get_lets_decentr_page_subtitle(self):
        return self.get_text(self.LetsDecentrPageSubTitle)

    def get_restore_account_page_title(self):
        return self.get_text(self.RestoreAccountPageTitle)

    def get_restore_account_page_content(self):
        return self.get_text(self.RestoreAccountPageContent)

    def confirm_cookie(self):
        self.click_on(self.ConfirmCookieButton)

    def click_all_done_button(self):
        self.click_on(self.AllDoneButton)
