from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when
from time import sleep


@given("Open the main (log in) page")
def open_login_page(context):
    context.app.login_page.open_login_page()


@when("Log in to the page")
def click_sign_in(context):
    context.app.login_page.click_sign_in()
