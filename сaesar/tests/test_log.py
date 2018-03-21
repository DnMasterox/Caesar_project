from tests.test_base import TestBase
from front.pages.login_page import LogInPage
import time

import unittest


class TestLog(TestBase):

    # def test_login_in(self):
    #     """проверку добавить на факт нужной страницы"""
    #     groups_page = LogInPage(self.driver) \
    #         .user_name("dmytro") \
    #         .user_password('1234') \
    #         .submit_log_in().get_title_name()
    #     self.assertIn("Caesar", groups_page)
    #     time.sleep(5)

    def test_2(self):
        groups_page = LogInPage(self.driver) \
            .user_name("hello") \
            .user_password('1234') \
            .submit_log_in().my_group()


if __name__ == '__main__':
    unittest.main()
