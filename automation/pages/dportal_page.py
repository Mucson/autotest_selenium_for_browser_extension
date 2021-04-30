from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage


class dPortalPage(BasePage):

    PDVRateTab = (By.XPATH, "//a[@href='#/portal/pdv-rate']")
    ActivityTab = (By.XPATH, "//a[@href='#/portal/activity']")
    AssetsTab = (By.XPATH, "//a[@href='#/portal/assets']")
    SendButton = (By.XPATH, "//button[text()=' Send ']")
    BackButton = (By.XPATH, "")
    CancelButton = (By.XPATH, "//button[text()=' Cancel ']")
    AmountField = (By.XPATH, "//input[contains(@class, 'transfer-input')]")
    WalletAddressField = (By.XPATH, "//textarea[contains(@class, 'transfer-input')]")
    CopyWalletAddressButton = (By.XPATH, "//button[contains(@class, 'portal-page__copy-wallet-button')]")
    SuccessfulSendingInfoMessage = (By.XPATH, "//div[@role='alertdialog']")

    def open_assets_tab(self):
        self.click_on(self.AssetsTab)

    def click_send_button(self):
        self.click_on(self.SendButton)

    def input_amount_in_appropriate_field(self, amount):
        self.type_in(self.AmountField, amount)

    def input_wallet_address_in_appropriate_field(self, wallet_address):
        self.type_in(self.WalletAddressField, wallet_address)

    def copy_my_wallet_address(self):
        self.click_on(self.CopyWalletAddressButton)

    def get_successful_sending_message(self):
        self.get_text(self.SuccessfulSendingInfoMessage)
