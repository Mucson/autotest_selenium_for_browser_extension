import configparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chromeOptions = Options()
    chromeOptions.add_extension("/home/vladimir/Downloads/charon_chrome.zip")
    chromeOptions.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chromeOptions)
    context.driver.get("chrome://extensions/")
    extension_id = context.driver.execute_async_script(
        "return_var = arguments[0];const extensions = document.querySelector("
        "\"extensions-manager\").shadowRoot.querySelector( "
        "\"extensions-item-list\").shadowRoot.querySelectorAll(\"extensions-item\");for (let i = 0; i < "
        "extensions.length; i++) {const extension = extensions[i].shadowRoot;const name = "
        "extension.querySelector('#name').textContent; console.log(name);if (name === 'Charon') "
        "{ console.log(extensions[i].getAttribute(\"id\"));return_var(extensions[i].getAttribute(\"id\"))}} return "
        "undefined")
    context.driver.get('chrome-extension://' + extension_id + '/charon/index.html#/welcome')
    context.driver.implicitly_wait(10)

    parser = configparser.ConfigParser()
    parser.read("credentials.ini")
    context.config = parser


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_all(context):
    context.driver.quit()
