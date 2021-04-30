import time

from behave import *
from automation.pages.dportal_page import dPortalPage


@when("I open Assets tab")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.open_assets_tab()


@when("I click Send button")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.click_send_button()
    time.sleep(2)


@when("I input amount")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.input_amount_in_appropriate_field(context.config.get("assets", "amount"))


@when("I input wallet address")
def step_impl(context):
    dportal_page = dPortalPage(context.driver)
    dportal_page.input_wallet_address_in_appropriate_field(context.config.get("assets", "wallet_address"))


@when('I input "{amount}" in amount field')
def step_impl(context, amount):
    dportal_page = dPortalPage(context.driver)
    dportal_page.input_amount_in_appropriate_field(amount)


@when('I input "{wallet_address}" in wallet address field')
def step_impl(context, wallet_address):
    dportal_page = dPortalPage(context.driver)
    dportal_page.input_wallet_address_in_appropriate_field(wallet_address)


@then("I see validation message for amount field")
def step_impl(context):
    for row in context.table:
        context.execute_steps('''
        When I input "{amount}" in amount field
        Then I see element with text "{text}"
        '''.format(amount=row["amount"], text=row["text"]))


@then("I see validation message for wallet address field")
def step_impl(context):
    for row in context.table:
        context.execute_steps('''
        When I input "{wallet_address}" in wallet address field
        Then I see element with text "{text}"
        '''.format(wallet_address=row["wallet_address"], text=row["text"]))
