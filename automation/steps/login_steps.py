import time

from behave import *
from automation.pages.login_page import LoginPage


@given("I click Get Started button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_get_started_button()


@when("I click Import account button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_import_account_button()


@when("I type credentials")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_seed_phrase(context.config.get("user", "seed_phrase"))
    login_page.enter_password(context.config.get("user", "password"))
    login_page.enter_confirm_password(context.config.get("user", "confirm_password"))


@when("I click Import account")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_import_account()


@then("I verify I am on the dhub page")
def step_impl(context):
    assert "Charon" in context.driver.title


@given("I imported my account")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_get_started_button()
    login_page.click_on_import_account_button()
    login_page.enter_seed_phrase(context.config.get("user", "seed_phrase"))
    login_page.enter_password(context.config.get("user", "password"))
    login_page.enter_confirm_password(context.config.get("user", "confirm_password"))
    login_page.click_on_import_account()


@when("I click lock account")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.lock_account()
    assert "Let's Decentr!" in login_page.get_lets_decentr_page_title()
    assert "The decentralized data market" in login_page.get_lets_decentr_page_subtitle()
    time.sleep(2)


@when("I click restore account")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.restore_account_init()
    time.sleep(1)


@when("I click back")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_back_button()


@when("I fill in the password")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_password(context.config.get("user", "password"))


@when("I click unlock")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.unlock_account()


@then("I assert I am on the correct page")
def step_impl(context):
    login_page = LoginPage(context.driver)
    assert "Restore an account with a seed phrase" in login_page.get_restore_account_page_title()
    assert "Enter your secret 24 word phrase in the field below to restore your account." \
           in login_page.get_restore_account_page_content()


@when("I click restore button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.restore_account()
