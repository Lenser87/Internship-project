from pages.base_page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    SIGN_IN_BTN = (By.XPATH, "//div[text()='Sign in']")
    EMAIL_FLD = (By.ID, "email-2")
    PWD_FLD = (By.ID, "field")
    CONTINUE_BTN = (By.XPATH, "//a[@wized='loginButton']")


    def open_login_page(self):
        self.open("https://soft.reelly.io/sign-up")

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN_BTN)
        self.input_text('lenser87@mail.ru',*self.EMAIL_FLD)
        self.input_text('8719rjlQ.', *self.PWD_FLD)
        self.wait_until_clickable_click(*self.CONTINUE_BTN)
