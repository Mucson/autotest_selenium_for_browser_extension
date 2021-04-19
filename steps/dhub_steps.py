from behave import *
from Charon.pages.dhub_page import dHubPage


@when("I click New Post button")
def step_impl(context):
    dhub_page = dHubPage(context.driver)
    dhub_page.click_new_post_button()
    dhub_page.enter_post_info("TestAutomation is coming", "We are introducing auto test")
    dhub_page.click_publish_post_button()


@when("I delete published post")
def step_impl(context):
    dhub_page = dHubPage(context.driver)
    dhub_page.go_to_latest_posts_page_and_choose_published_post()
    dhub_page.cancel_delete_button()
    dhub_page.click_delete_button()