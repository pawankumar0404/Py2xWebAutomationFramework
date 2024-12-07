from behave import given,when,then

@given('open the app.vwo.com')
def step_impl(context):
    pass

@when('I enter {username} and {password}')
def step_impl(context,username,password):
    print(username,password)

@then('I get this {message}')
def step_impl(context,message):
    print(message)