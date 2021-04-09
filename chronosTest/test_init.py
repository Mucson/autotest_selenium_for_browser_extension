import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chronosTest.Pages.dhub_page import dHubPage
from chronosTest.Pages.login_page import LoginPage
from chronosTest.Pages.account_details_page import AccountDetailsPage

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

# initialization classes and methods
login_page = LoginPage(driver)
account_details_page = AccountDetailsPage(driver)
dhub_page = dHubPage(driver)

# login into the system
assert "Welcome to Decentr" in login_page.get_welcome_message_title()
login_page.click_on_get_started_button()
login_page.click_on_import_account_button()
login_page.enter_seed_phrase("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
                             "physical wolf poem letter panel embrace explain scissors have mosquito inner")
login_page.enter_password("123456aA!")
login_page.enter_confirm_password("123456aA!")
login_page.click_on_import_account()
assert "Charon" in driver.title

# account details page test
dhub_page.open_small_menu()
account_details_page.go_to_account_details()
time.sleep(1)
assert "Account details" in account_details_page.get_account_details_page_title()
account_details_page.enter_first_name("Test")
account_details_page.enter_last_name("Automation")
account_details_page.select_gender_male()
account_details_page.select_gender_female()
account_details_page.enter_bio_field("We are introducing automation in your business!")
account_details_page.enter_nickname("Test_automation_user")
account_details_page.enter_new_password("123456aA!")
account_details_page.confirm_password("123456aA!")
account_details_page.click_save_button()
time.sleep(6)
assert "User was successfully updated" in account_details_page.get_successful_user_update_message()
account_details_page.click_back_button()

# lock and unlock account
time.sleep(2)
dhub_page.open_small_menu()
time.sleep(1)
login_page.lock_account()
time.sleep(1)
assert "Let's Decentr!" in login_page.get_lets_decentr_page_title()
assert "The decentralized data market" in login_page.get_lets_decentr_page_subtitle()
login_page.enter_password("123456aA!")
time.sleep(1)
login_page.unlock_account()
time.sleep(1)

# lock and restore account
dhub_page.open_small_menu()
time.sleep(1)
login_page.lock_account()
login_page.restore_account_init()
login_page.click_back_button()
time.sleep(1)
login_page.restore_account_init()
time.sleep(1)

assert "Restore an account with a seed phrase" in login_page.get_restore_account_page_title()
assert "Enter your secret 24 word phrase in the field below to restore your account." \
       in login_page.get_restore_account_page_content()

login_page.enter_seed_phrase("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
                             "physical wolf poem letter panel embrace explain scissors have mosquito inner")
login_page.enter_password("123456aA!")
login_page.enter_confirm_password("123456aA!")
login_page.restore_account()
time.sleep(1)

# publish post
dhub_page.click_new_post_button()
dhub_page.enter_post_info("TestAutomation is coming", "We are introducing auto test")
dhub_page.click_publish_post_button()
time.sleep(6)
assert "Post has been created successfully" in dhub_page.get_successful_publish_post_message()

# delete published post
time.sleep(2)
dhub_page.go_to_latest_posts_page_and_choose_published_post()
time.sleep(1)
dhub_page.cancel_delete_button()
time.sleep(1)
dhub_page.click_delete_button()
time.sleep(4)
assert "Post has been removed successfully" in dhub_page.get_successful_delete_post_message()

driver.quit()
