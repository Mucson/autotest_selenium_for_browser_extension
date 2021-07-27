from behave import *

from automation.pages.user_page import UserPage


@when("I open user profile page")
def step_impl(context):
    user_page = UserPage(context.driver)
    user_page.edit_profile()
