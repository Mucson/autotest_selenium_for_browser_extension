import time

from behave import *

from automation.pages.user_page import UserPage


@when("I open user profile page")
def step_impl(context):
    user_page = UserPage(context.driver)
    user_page.edit_profile()


@given("I open small menu")
def step_impl(context):
    user_page = UserPage(context.driver)
    user_page.open_small_menu()
    time.sleep(1)


@when("I open menu")
def step_impl(context):
    user_page = UserPage(context.driver)
    user_page.open_small_menu()
    time.sleep(1)
