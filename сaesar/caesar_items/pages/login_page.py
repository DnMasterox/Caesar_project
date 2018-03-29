from caesar_items.pages.base_page import BasePage
from caesar_items.locators.locators import LogInLocators
from caesar_items.pages.groups_page import GroupsPage


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, user_login=''):
        self.driver.find_element(*LogInLocators.LOGIN_FIELD).clear()
        return self.driver.find_element(*LogInLocators.LOGIN_FIELD).\
            send_keys(user_login)

    def enter_password(self, user_password=''):
        self.driver.find_element(*LogInLocators.PASSWORD_FIELD).clear()
        return self.driver.find_element(*LogInLocators.PASSWORD_FIELD).\
            send_keys(user_password)

    def message(self):
        return self.driver.find_element(*LogInLocators.FIELD_MESSAGE).text

    def submit_button_element(self):
        return self.driver.find_element(*LogInLocators.CONFIRM_ACTION)

    def open_group_page(self):
        self.driver.find_element(*LogInLocators.CONFIRM_ACTION).click()
        self.driver.implicitly_wait(2)
        return GroupsPage(self.driver)

    def auto_login(self, user):
        self.enter_login(user.login)
        self.enter_password(user.password)
        self.open_group_page()
        self.driver.implicitly_wait(5)


