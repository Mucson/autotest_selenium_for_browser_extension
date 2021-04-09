import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chromeOptions = Options()
chromeOptions.add_extension("/home/vladimir/Downloads/charon_extension.zip")
chromeOptions.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chromeOptions)

driver.get("chrome://extensions/")
driver.implicitly_wait(10)

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

SeedPhraseField = driver.find_element_by_xpath(
    "//input[@data-placeholder='Separate each word with a single space']")
SeedPhraseField.send_keys("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
                          "physical wolf poem letter panel embrace explain scissors have mosquito inner")

PasswordField = driver.find_element_by_xpath("//input[@name='password']")
PasswordField.send_keys("123456aA!")
ConfirmPasswordField = driver.find_element_by_xpath("//input[@name='confirmPassword']")
ConfirmPasswordField.send_keys("123456aA!")
ImportButton = driver.find_element_by_xpath("//*[text()=' IMPORT ']").click()


# smallMenu = driver.find_element_by_xpath("//div[@class='mat-menu-trigger menu__trigger ng-star-inserted']").click()
# time.sleep(2)
# LockAccountButton = driver.find_element_by_xpath("//*[text()='Lock account']").click()
# RestoreAccountButton = driver.find_element_by_xpath("//a[text()='Restore Your Account']").click()
# time.sleep(2)
# SeedPhraseField = driver.find_element_by_xpath(
#     "//input[@data-placeholder='Separate each word with a single space']")
# SeedPhraseField.send_keys("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
#                           "physical wolf poem letter panel embrace explain scissors have mosquito inner")
# PasswordField = driver.find_element_by_xpath("//input[@name='password']")
# PasswordField.send_keys("123456aA!")
# ConfirmPasswordField = driver.find_element_by_xpath("//input[@name='confirmPassword']")
# ConfirmPasswordField.send_keys("123456aA!")
# RestoreButton = driver.find_element_by_xpath("//*[text()=' RESTORE ']").click()

time.sleep(2)

topPostsBar = driver.find_elements_by_xpath("//div[@class='posts-page__section-right']//app-hub-top-posts["
                                            "@class='ng-star-inserted']")
count_post = len(topPostsBar)
print(count_post)
