from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class dHubPage(BasePage):

    SmallMenuOpenButton = (By.XPATH, "//div[contains(@class, 'menu__trigger')]")
    NewPostButton = (By.XPATH, "//*[text()=' New post ']")
    ChoosePostTopicButton = (By.XPATH, "//mat-select[contains(@class,'mat-select')]")
    ChoosePostTopic = (By.XPATH, "//span[text()='Science & Technology']")
    TitleField = (By.XPATH, "//textarea[@placeholder='Title']")
    BodyPostTextField = (By.XPATH, "//div[@data-placeholder='Start your post with...']")
    PublishPostButton = (By.XPATH, "//button[@form='POST_CREATE_FORM']")
    LatestNewsTab = (By.XPATH, "//a[@href='#/hub/posts']")
    PublishedPost = (By.XPATH, "//div[text()=' TestAutomation is coming ']")
    DeletePostButton = (By.XPATH, "//*[text()=' Delete post ']")
    CancelDeleteButton = (By.XPATH, "//div[text()=' Cancel ']")
    ConfirmDeleteButton = (By.XPATH, "//div[text()=' Delete ']")
    SuccessfulPublishPostMessage = (By.XPATH, "//div[@role='alertdialog']")
    SuccessfulDeletePostMessage = (By.XPATH, "//div[@role='alertdialog']")
    dPortalPageButton = (By.XPATH, "//div[@data-id='dportal']")

    def open_small_menu(self):
        self.click_on(self.SmallMenuOpenButton)

    def click_new_post_button(self):
        self.click_on(self.NewPostButton)

    def enter_post_info(self, title, text):
        self.click_on(self.ChoosePostTopicButton)
        self.click_on(self.ChoosePostTopic)
        self.type_in(self.TitleField, title)
        self.type_in(self.BodyPostTextField, text)

    def click_publish_post_button(self):
        self.click_on(self.PublishPostButton)

    def get_successful_publish_post_message(self):
        return self.get_text(self.SuccessfulPublishPostMessage)

    def go_to_latest_posts_page_and_choose_published_post(self):
        self.click_on(self.LatestNewsTab)
        self.click_on(self.PublishedPost)

    def cancel_delete_button(self):
        self.click_on(self.DeletePostButton)
        self.click_on(self.CancelDeleteButton)

    def click_delete_button(self):
        self.click_on(self.DeletePostButton)
        self.click_on(self.ConfirmDeleteButton)

    def get_successful_delete_post_message(self):
        return self.get_text(self.SuccessfulDeletePostMessage)

    def click_dportal_page_button(self):
        self.click_on(self.dPortalPageButton)
