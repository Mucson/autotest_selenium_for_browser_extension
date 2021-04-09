import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chronosTest.Pages.dhub_page import dHubPage
from chronosTest.Pages.login_page import LoginPage
from chronosTest.Pages.user_menu_page import UserMenu

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

login_page = LoginPage(driver)
login_page.click_on_get_started_button()
login_page.click_on_import_account_button()
login_page.enter_seed_phrase("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
                             "physical wolf poem letter panel embrace explain scissors have mosquito inner")
login_page.enter_password("123456aA!")
login_page.enter_confirm_password("123456aA!")
login_page.click_on_import_account()

assert "Charon" in driver.title

# account details page test
user_menu_page = UserMenu(driver)
login_page.open_small_menu()
time.sleep(1)
user_menu_page.go_to_account_details()
time.sleep(1)
user_menu_page.enter_first_name("Test")
user_menu_page.enter_last_name("Automation")
user_menu_page.select_gender_male()
user_menu_page.select_gender_female()
user_menu_page.enter_bio_field("We are introducing automation in your business!")
user_menu_page.enter_nickname("Test_automation_user")
user_menu_page.enter_new_password("123456aA!")
user_menu_page.confirm_password("123456aA!")
user_menu_page.click_save_button()
time.sleep(5)
assert "User was successfully updated" in user_menu_page.get_successful_user_update_message()
user_menu_page.click_back_button()

# lock and unlock account
time.sleep(2)
login_page.open_small_menu()
time.sleep(1)
login_page.lock_account()
time.sleep(1)
login_page.enter_password("123456aA!")
login_page.unlock_account()
time.sleep(1)

# lock and restore account
login_page.open_small_menu()
time.sleep(1)
login_page.lock_account()
login_page.restore_account_init()
login_page.enter_seed_phrase("life shoe such cram shed enroll leaf consider coyote spider reveal galaxy point "
                             "physical wolf poem letter panel embrace explain scissors have mosquito inner")
login_page.enter_password("123456aA!")
login_page.enter_confirm_password("123456aA!")
login_page.restore_account()
time.sleep(1)

# publish post
dhub_page = dHubPage(driver)
dhub_page.click_new_post_button()
dhub_page.enter_post_info("TestAutomation is coming", "We are introducing auto test")
dhub_page.click_publish_post_button()
time.sleep(2)
# assert "Post has been created successfully" in dhub_page.get_successful_publish_post_message()

# delete published post
time.sleep(3)
dhub_page.go_to_latest_posts_page_and_choose_published_post()
time.sleep(1)
dhub_page.cancel_delete_button()
time.sleep(1)
dhub_page.click_delete_button()
# assert "Post has been removed successfully" in dhub_page.get_successful_delete_post_message()

driver.quit()
