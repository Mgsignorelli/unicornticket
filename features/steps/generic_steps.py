from behave import *
import django.contrib.auth.models


@given(u'I {model_type} a {model} with {attribute} of {value}')
def step_impl(context, model_type, model, attribute, value):
    model_map = {
        'user': django.contrib.auth.models.User
    }

    try:
        model_instance = model_map[model].objects.get(**{attribute+'__iexact': value})
    except model_map[model].DoesNotExist:
        model_instance = model_map[model]
        setattr(model_instance, attribute, value)

    if model == 'user':
        model_instance.password = 'password'

    if model_type == 'am':
        context.model = model_instance

    else:
        context.models[model] = model_instance
