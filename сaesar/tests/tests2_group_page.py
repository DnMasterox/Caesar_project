from resource.users_base import *
from tests.test_base import TestBase
from caesar_items.pages.groups_page import GroupsPage
from caesar_items.pages.login_page import LogInPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time

import unittest

expected_url = 'http://localhost:3000/Groups/Dnipro'
expected_title_login_page = 'Log in - Caesar'


class TestGroupPage(TestBase):

    def test17_logout_top_menu(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        top_menu = group_page.top_menu_open()
        top_menu.log_out_click()
        self.assertEqual(self.driver.title, expected_title_login_page)

    def test18_logout_right_menu(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        right_menu = group_page.right_menu_open()
        login_page = right_menu.log_out_click()
        self.assertEqual(login_page.get_title_name(), expected_title_login_page)

    def test19_open_about(self):
        expected_page_url = 'http://localhost:3000/About'
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        top_menu = group_page.top_menu_open()
        top_menu.about()
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test20_open_schedule(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        top_menu = group_page.top_menu_open()
        top_menu.schedule()
        expected_page_url = 'http://localhost:3000/Schedule/' + first_admin.location
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test21_open_students(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        top_menu = group_page.top_menu_open()
        top_menu.students()
        expected_page_url = 'http://localhost:3000/Students/' + first_admin.location
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test22_open_groups(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        top_menu = group_page.top_menu_open()
        top_menu.groups()
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test23_open_locations(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        top_menu = group_page.top_menu_open()
        top_menu.locations()
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location + '/locations'
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test24_open_create_page_for_admin(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        left_menu = group_page.left_menu_open()
        time.sleep(1)
        left_menu.create_group().click()
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location + '/new'
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test24_open_create_page_for_coordinator(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        left_menu = group_page.left_menu_open()
        left_menu.create_group().click()
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location + '/new'
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test25_disabled_create_button_for_teacher(self):
        teacher.auto_login_n_open_group_page(self.login_page)
        group_page = GroupsPage(self.driver)
        left_menu = group_page.left_menu_open()
        time.sleep(1)
        try:
            left_menu.create_group().is_displayed()
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
