from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    OFF_PLAN_BTN = (By.XPATH, "//div[text()='Off-plan']")
    TOTAL_PROJECTS_FLD = (By.XPATH, "//div[text()='Total projects']")
    FILTERS_BTN = (By.CSS_SELECTOR, "a.filter-button.w-inline-block")
    OUT_OF_STOCK_BTN = (By.CSS_SELECTOR, "div[wized='priorityStatusOutOfStock'][class*='margin-bottom-8']")
    APPLY_FILTER_BTN = (By.XPATH, "//a[text()='Apply filter']")
    OUT_OF_STOCKS_FLD = (By.CSS_SELECTOR, "div[wized='projectMinimumPrice'][class='price-value']")
    MAP_VIEW_BTN = (By.XPATH, "//div[text()='Map view']")


    def click_off_plan(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_BTN)

    def go_to_map_page(self):
        self.wait_until_clickable_click(*self.MAP_VIEW_BTN)

    def verify_main_page(self):
        self.verify_text('Total projects', *self.TOTAL_PROJECTS_FLD)

    def filter_out_of_stock(self):
        self.wait_until_clickable_click(*self.FILTERS_BTN)
        self.wait_until_clickable_click(*self.OUT_OF_STOCK_BTN)
        self.wait_until_clickable_click(*self.APPLY_FILTER_BTN)

    def verify_out_of_stocks_tag(self):
        expected_tag = 'Out of stock'
        out_of_stock_elements = self.find_elements(*self.OUT_OF_STOCKS_FLD)
        for each_tag in out_of_stock_elements:
            actual_tag = each_tag.text
            if expected_tag == actual_tag:
                print(expected_tag)
