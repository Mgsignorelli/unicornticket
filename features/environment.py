import os
from behave import *
from behave.model_core import Status
from splinter import Browser


@fixture
def web_browser(context):
    context.browser = Browser('chrome', headless=True, incognito=True)

    yield context.browser
    context.browser.quit()


@fixture
def clean_screenshots(context):
    dir_name = os.path.dirname(os.path.realpath(__file__)) + '/screenshots/'

    for item in os.listdir(dir_name):
        if item.endswith(".png"):
            os.remove(os.path.join(dir_name, item))


def before_all(context):
    context.fixtures = ['accounts.yaml', 'bugs.yaml', 'features.yaml']
    context.models = {}
    use_fixture(clean_screenshots, context)
    use_fixture(web_browser, context)


def after_step(context, current_step):
    if current_step.status == Status.failed:
        dir_name = os.path.dirname(os.path.realpath(__file__)) + '/screenshots/'
        file_name = current_step.keyword + ' ' + current_step.name
        context.browser.screenshot(dir_name + file_name + '.png')
