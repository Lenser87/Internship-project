from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.map_view_page import MapViewPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.map_view_page = MapViewPage(driver)
