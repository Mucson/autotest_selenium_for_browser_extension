from selenium import webdriver


def before_all():
    pass


def after_all(context):
    context.driver.quit()
    pass
