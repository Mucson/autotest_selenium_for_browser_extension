import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from chronosTest.Pages.base_page import BasePage

chromeOptions = Options()
chromeOptions.add_extension("/home/vladimir/Downloads/charon_extension.zip")
chromeOptions.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chromeOptions)
driver.implicitly_wait(10)

driver.get("chrome://extensions/")


extension_id = driver.execute_async_script(
    "return_var = arguments[0];const extensions = document.querySelector("
    "\"extensions-manager\").shadowRoot.querySelector( "
    "\"extensions-item-list\").shadowRoot.querySelectorAll(\"extensions-item\");for (let i = 0; i < "
    "extensions.length; i++) {const extension = extensions[i].shadowRoot;const name = "
    "extension.querySelector('#name').textContent; console.log(name);if (name === 'Charon') "
    "{ console.log(extensions[i].getAttribute(\"id\"));return_var(extensions[i].getAttribute(\"id\"))}} return "
    "undefined")

driver.get('chrome-extension://' + extension_id + '/charon/index.html#/welcome')

assert "Charon" in driver.title

STARTED_BUTTON = driver.find_element_by_xpath("//*[text()=' Get Started ']").click()
IMPORT_ACCOUNT = driver.find_element_by_xpath("//*[text()=' Import Account ']").click()

# CreateAccountButton = driver.find_element_by_xpath("//*[text()=' Create an Account ']").click()

SeedPhraseField = driver.find_element_by_xpath(
    "//input[@data-placeholder='Separate each word with a single space']")
SeedPhraseField.send_keys("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
                          "physical wolf poem letter panel embrace explain scissors have mosquito inner")

PasswordField = driver.find_element_by_xpath("//input[@name='password']")
PasswordField.send_keys("123456aA!")
ConfirmPasswordField = driver.find_element_by_xpath("//input[@name='confirmPassword']")
ConfirmPasswordField.send_keys("123456aA!")
ImportButton = driver.find_element_by_xpath("//*[text()=' IMPORT ']").click()


# dHub page


hubWorldNews = driver.find_element_by_xpath("//a[@href='#/hub/posts/1']").click()

HubTravelTourism = driver.find_element_by_xpath("//a[@href='#/hub/posts/2']").click()
# assert "Travel & Tourism" in driver.data-title  color is #03b15e

HubScienceTechnology = driver.find_element_by_xpath("//a[@href='#/hub/posts/3']").click()
# assert "Science & Technology" in driver.data-title  color is #fa5454

HubStrangeWorld = driver.find_element_by_xpath("//a[@href='#/hub/posts/4']").click()
# assert "Strange World" in driver.data-title  color is #ff8c04

HubArtsEntertainment = driver.find_element_by_xpath("//a[@href='#/hub/posts/5']").click()
# assert "Arts & Entertainment" in driver.data-title  color is #f8d72a

HubWritersWriting = driver.find_element_by_xpath("//a[@href='#/hub/posts/6']").click()
# assert "Writers & Writing" in driver.data-title  color is #73d1f9

HubHealthFitness = driver.find_element_by_xpath("//a[@href='#/hub/posts/7']").click()
# assert "Health & Fitness" in driver.data-title  color is #9f65fd

HubCryptoBlockchain = driver.find_element_by_xpath("//a[@href='#/hub/posts/8']").click()
# assert "Crypto & Blockchain" in driver.data-title  color is #e87cc9

HubSports = driver.find_element_by_xpath("//a[@href='#/hub/posts/9']").click()
# assert "Sports" in driver.data-title  is #3edcd3

HubLatestPosts = driver.find_element_by_xpath("//a[@href='#/hub/posts']")
HubLatestPosts.click()

# dPortalPage = driver.find_element_by_xpath("//*[text()='dPortal']")
# dPortalPage.click()

count = len(driver.find_elements_by_xpath("//div[@class='posts-page__posts-grid"
                                          "-container']//app-hub-post-card[ "
                                          "@class='posts-page__post-card "
                                          "mod-vertical ng-star-inserted']"))
print("Quantity posts on the top page is", count)

assert count == 8

NewPostButton = driver.find_element_by_xpath("//*[text()=' New post ']").click()
PublishPostButton = driver.find_element_by_xpath("//button[@form='POST_CREATE_FORM']")
PublishPostButton.click()

# label_error = driver.find_elements_by_xpath("//app-form-error[@class='hub-post-editor-error typeface-caption "
#                                            "ng-star-inserted']")
# print(label_error)

topicDropdown = driver.find_element_by_xpath("//app-hub-category-select[@formcontrolname='category']").click()
topicList = driver.find_element_by_xpath("//span[text()='Science & Technology']").click()

titleField = driver.find_element_by_xpath("//textarea[@placeholder='Title']")
titleField.send_keys("TestAutomation is coming")

textBodyField = driver.find_element_by_xpath("//div[@data-placeholder='Start your post with...']")
textBodyField.send_keys("We are introducing auto test")

PublishPostButton.click()

# //div[text()='Post has been created successfully']
# assert "Post has been created successfully" in driver.page_source

time.sleep(4)
# delete my post
# HubLatestPosts.click()
MyPostCard = driver.find_element_by_xpath("//div[text()=' TestAutomation is coming ']").click()
DeletePostButton = driver.find_element_by_xpath("//*[text()=' Delete post ']").click()
ConfirmDeletePostButton = driver.find_element_by_xpath("//div[text()=' Delete ']").click()
assert "Post has been removed successfully" in driver.page_source


# Small menu

# smallMenu = driver.find_element_by_xpath("//div[@class='mat-menu-trigger menu__trigger ng-star-inserted']")
# smallMenu.click()
#
# # Lock, Unlock, Restore account
# time.sleep(1)
# LockAccountButton = driver.find_element_by_xpath("//*[text()='Lock account']")
# LockAccountButton.click()
# PasswordField = driver.find_element_by_xpath("//input[@name='password']")
# time.sleep(1)
# PasswordField.send_keys("123456aA!")
# time.sleep(1)
# UnlockButton = driver.find_element_by_xpath("//*[text()=' UNLOCK ']").click()
#
# time.sleep(3)
# smallMenuMenu = driver.find_element_by_xpath("//div[@class='mat-menu-trigger menu__trigger ng-star-inserted']").click()
# time.sleep(2)
# LockAccountButton.click()
# RestoreAccountButton = driver.find_element_by_xpath("//a[text()='Restore Your Account']").click()
# SeedPhraseField.send_keys("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
#                           "physical wolf poem letter panel embrace explain scissors have mosquito inner")
# PasswordField.send_keys("123456aA!")
# ConfirmPasswordField.send_keys("123456aA!")
# RestoreButton = driver.find_element_by_xpath("//*[text()=' RESTORE ']").click()

# assert label_error.text == " Post topic is required "

# driver.quit()
