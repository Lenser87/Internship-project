from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@then ("Verify Map page is opened")
def verify_map_page(context):
    context.app.map_view_page.verify_map_page()