from behave import *
import requests


@when('I send owner to host')
def step_impl(context):
    url = context.base_url + "/auth/accounts/decentr1cehgxxyskvn39f9sj46jqjewp805x4prad6ds5"
    r = requests.get(url)
    assert r.status_code == 200

    context.token = r.json()["result"]["value"]["public_key"]
    print(context.token)
