from behave import *


@when(u'I navigate to {destination} with id {id}')
def step_impl(context, destination, id):
    context.browser.visit(context.get_url(destination, id=id))


@when(u'I navigate to {destination}')
def step_impl(context, destination):
    context.browser.visit(context.get_url(destination))


@when(u'I enter "{value}" into the {field} field of the {form} form')
def step_imp(context, value, field, form):
    context.browser.fill_form({field: value}, name=form)


@when(u'I choose "{value}" from the choices in the {field} field of the {form} form')
def step_imp(context, value, field, form):
    context.browser.choose(field, value)


@when(u'I select "{value}" from the choices in the {field} field of the {form} form')
def step_imp(context, value, field, form):
    context.browser.select(field, value)


@when(u'I enter {model_type} {attribute} {validity} into the {field} field of the {form} form')
def step_impl(context, model_type, attribute, validity, field, form):
    if model_type == 'my':
        model = context.model
    else:
        model = context.models[model_type]

    if validity == 'correctly':
        context.browser.fill_form({field: getattr(model, attribute)}, name=form)
    else:
        context.browser.fill_form({field: 'random incorrect string'}, name=form)


@when(u'I enter {model_type} {attribute} {validity} in the {form} form')
def step_impl(context, model_type, attribute, validity, form):
    if model_type == 'my':
        model = context.model
    else:
        model = context.models[model_type]

    if validity == 'correctly':
        context.browser.fill_form({attribute: getattr(model, attribute)}, name=form)
    else:
        context.browser.fill_form({attribute: 'random incorrect string'}, name=form)


@when(u'I submit the {name} form')
def step_impl(context, name):
    context.browser.find_by_css('form[name="' + name + '"] button[type="submit"]').first.click()


@then(u'I {told} told "{message}"')
def step_impl(context, told, message):
    told = told == 'should be'
    found = context.browser.is_text_present(message)
    assert told and found or not told and not found
