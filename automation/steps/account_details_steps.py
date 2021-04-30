import time

from behave import *

from automation.pages.dhub_page import dHubPage
from automation.pages.account_details_page import AccountDetailsPage


@given("I open menu")
def step_impl(context):
    dhub_page = dHubPage(context.driver)
    dhub_page.open_small_menu()
    time.sleep(1)


@when("I open menu")
def step_impl(context):
    dhub_page = dHubPage(context.driver)
    dhub_page.open_small_menu()
    time.sleep(1)


@when("I open account details page")
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.go_to_account_details()


@when('I fill in the first name field')
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.enter_first_name(context.config.get("account", "first_name"))


@when('I fill in the last name field')
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.enter_last_name(context.config.get("account", "last_name"))


@when("I select gender")
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.select_gender_male()
    account_details_page.select_gender_female()


@when('I fill in the bio field')
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.enter_bio_field(context.config.get("account", "bio_info"))


@when('I fill in the nickname field')
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.enter_nickname(context.config.get("account", "nickname"))


@when('I fill in the password field')
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.enter_new_password(context.config.get("account", "password"))


@when('I fill in the confirm password field')
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.confirm_new_password(context.config.get("account", "confirm_password"))


@when("I click Save button")
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.click_save_button()


@when("I fill in the account details page")
def step_impl(context):
    account_details_page = AccountDetailsPage(context.driver)
    account_details_page.enter_first_name(context.config.get("account", "first_name"))
    account_details_page.enter_last_name(context.config.get("account", "last_name"))
    account_details_page.select_gender_male()
    account_details_page.select_gender_female()
    account_details_page.enter_bio_field(context.config.get("account", "bio_info"))
    account_details_page.enter_nickname(context.config.get("account", "nickname"))
    account_details_page.enter_new_password(context.config.get("account", "password"))
    account_details_page.confirm_new_password(context.config.get("account", "confirm_password"))
