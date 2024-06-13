from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MapViewPage(Page):

    def verify_map_page(self):
        self.verify_partial_url("map")