import unittest
from time import sleep

from page.page_login import PageLogin
from base.get_driver import GetDriver
from parameterized import parameterized

from page.page_shopping import PageShopping
from page.page_order import PageOrder
from tool.read_json import read_json


def get_data():
    arrs = []
    for data in read_json("login.json").values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("expect_success"),
                     data.get("success"),
                     data.get('commodity'),
                     data.get('purchase_password')))

    return arrs


class TestLogin(unittest.TestCase):
    login = None

    @classmethod
    def setUpClass(cls):
        cls.login = PageLogin(GetDriver.get_driver())
        cls.login.page_click_login_link()
        cls.shopping = PageShopping(GetDriver.get_driver())
        cls.order = PageOrder(GetDriver.get_driver())

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, password, commodity, purchase_password):
        self.login.page_login(username, password)
        self.shopping.page_shopping(commodity)
        self.order.page_order(purchase_password)
        sleep(3)

