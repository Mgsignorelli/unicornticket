from behave import *
from splinter import Browser


@fixture
def web_browser(context):
    context.browser = Browser()
    yield context.browser
    context.browser.quit()


@fixture
def clean_screenshots(context):
    dir_name = os.path.dirname(os.path.realpath(__file__)) + '/screenshots/'

    for item in os.listdir(dir_name):
        if item.endswith(".png"):
            os.remove(os.path.join(dir_name, item))


def before_all(context):
    use_fixture(clean_screenshots, context)
    use_fixture(web_browser, context)
