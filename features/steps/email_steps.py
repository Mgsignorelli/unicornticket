from behave import *
from django.core import mail


@then(u'I should have received an email with a subject containing "{contents}"')
def step_impl(context, contents):
    assert contents in mail.outbox[0].subject


@then(u'I should not have received an email')
def step_impl(context):
    assert len(mail.outbox) == 0
