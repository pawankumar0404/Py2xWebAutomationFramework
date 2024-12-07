from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    pass


@when('we say {greeting}')
def step_impl(context, greeting):
    context.greeting = greeting


@then('behave should respond with {response}')
def step_impl(context, response):
    expected_response = {
        "Hello": "Hi there!",
        "Goodbye": "see you later!",
        "thanks": "you're welcome!"
    }
    assert expected_response.get(context.greeting, '') == response
