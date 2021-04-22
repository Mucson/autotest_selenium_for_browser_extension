from behave import *
from pages.dportal_page import dPortalPage


@when("I open Assets tab")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.open_assets_tab()


@when("I click Send button")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.click_send_button()


@when("I input amount")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.input_amount_in_appropriate_field(context.config.get("assets", "amount"))


@when("I input wallet address")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.input_wallet_address_in_appropriate_field(context.config.get("assets", "wallet_address"))
