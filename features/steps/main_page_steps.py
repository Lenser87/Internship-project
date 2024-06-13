from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Click on “off plan” at the left side menu")
def click_off_plan(context):
    context.app.main_page.click_off_plan()


@when("Filter by sale status of “Out of Stocks”")
def filter_out_of_stock(context):
    context.app.main_page.filter_out_of_stock()


@when("Go to Map page")
def go_to_map_page(context):
    context.app.main_page.go_to_map_page()


@then("Verify the right page opens")
def verify_main_page(context):
    context.app.main_page.verify_main_page()


@then("Verify each product contains the Out of Stocks tag")
def verify_out_of_stocks_tag(context):
    context.app.main_page.verify_out_of_stocks_tag()


