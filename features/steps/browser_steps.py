from behave import *


@when(u'I navigate to {destination}')
def step_impl(context, destination):
    context.browser.visit(context.get_url(destination))


@when(u'I enter "{value}" into the {field} field')
def step_imp(context, value, field):
    context.browser.fill(field, value)


@when(u'I enter {model_type} {attribute} {validity} into the {field} field')
def step_impl(context, model_type, attribute, validity, field):
    if model_type == 'my':
        model = context.model
    else:
        model = context.models[model_type]

    if validity == 'correctly':
        context.browser.fill(field, getattr(model, attribute))
    else:
        context.browser.fill(field, 'random incorrect string')


@when(u'I enter {model_type} {attribute} {validity}')
def step_impl(context, model_type, attribute, validity):
    if model_type == 'my':
        model = context.model
    else:
        model = context.models[model_type]

    if validity == 'correctly':
        context.browser.fill(attribute, getattr(model, attribute))
    else:
        context.browser.fill(attribute, 'random incorrect string')


@when(u'I submit the {name} form')
def step_impl(context, name):
    context.browser.find_by_css('form[name="' + name + '"] button[type="submit"]').first.click()


@then(u'I {told} told "{message}"')
def step_impl(context, told, message):
    told = told == 'should be'
    found = context.browser.is_text_present(message)
    assert told and found or not told and not found
