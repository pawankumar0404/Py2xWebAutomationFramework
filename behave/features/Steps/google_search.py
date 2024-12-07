from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('I am on the Google Home Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")


@when('I search for "{search_item}"')
def step_impl(context, search_item):
    search_box = context.driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_item)
    search_box.submit()


@then('I should see the "{expected_term}" in the result')
def step_impl(context, expected_term):
    assert expected_term in context.driver.page_source
    context.driver.quit()
