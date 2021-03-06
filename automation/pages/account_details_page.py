from automation.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountDetailsPage(BasePage):
    UserIconMenuButton = (By.XPATH, "//div[contains(@class,'menu__user-item ')]")
    FormFieldFirstName = (By.XPATH, "//div[text()='First Name']/..//input")
    FormFieldLastName = (By.XPATH, "//div[text()='Last Name']/..//input")
    GenderMale = (By.XPATH, "//mat-radio-button[@id='mat-radio-2']")
    GenderFemale = (By.XPATH, "//mat-radio-button[@id='mat-radio-3']")
    # GenderMale = (By.XPATH, "//mat-radio-button[@tabindex='-1'][1]")
    # GenderFemale = (By.XPATH, "//mat-radio-button[@tabindex='-1'][2]")
    BioField = (By.XPATH, "//textarea[@trim='blur']")
    EmailField = (By.XPATH, "//input[@type='email']")
    NewPasswordField = (By.XPATH, "//input[@formcontrolname='password']")
    ConfirmPasswordField = (By.XPATH, "//input[@formcontrolname='confirmPassword']")
    SaveButton = (By.XPATH, "//*[text()=' Save ']")
    SuccessfulUpdateUserInfoMessage = (By.XPATH, "//div[@role='alertdialog']")
    BackButton = (By.XPATH, "//div[contains(@class, 'btn__back')]")
    AccountDetailsPageTitle = (By.XPATH, "//div[contains(@class, 'page-title')]")

    def _verify_page_(self):
        self.on_this_page(self.FormFieldFirstName, self.FormFieldLastName, self.GenderMale, self.GenderFemale,
                          self.BioField, self.EmailField, self.NewPasswordField, self.ConfirmPasswordField,
                          self.SaveButton)

    def go_to_account_details(self):
        self.click_on(self.UserIconMenuButton)

    def enter_first_name(self, firstname):
        self.click_on(self.FormFieldFirstName)
        self.type_in(self.FormFieldFirstName, firstname)

    def enter_last_name(self, lastname):
        self.click_on(self.FormFieldLastName)
        self.type_in(self.FormFieldLastName, lastname)

    def select_gender_female(self):
        self.click_on(self.GenderFemale)

    def select_gender_male(self):
        self.click_on(self.GenderMale)

    def enter_bio_field(self, bio_info):
        self.click_on(self.BioField)
        self.type_in(self.BioField, bio_info)

    def enter_new_password(self, password):
        self.type_in(self.NewPasswordField, password)

    def confirm_new_password(self, password):
        self.type_in(self.ConfirmPasswordField, password)

    def click_save_button(self):
        self.click_on(self.SaveButton)

    def get_successful_user_update_message(self):
        return self.get_text(self.SuccessfulUpdateUserInfoMessage)

    def click_back_button(self):
        self.click_on(self.BackButton)

    def get_account_details_page_title(self):
        return self.get_text(self.AccountDetailsPageTitle)
