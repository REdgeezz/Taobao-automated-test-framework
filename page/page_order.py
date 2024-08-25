from time import sleep

from base.base import Base
import page


class PageOrder(Base):
    def page_btn_all_choose(self):
        self.base_click(page.order_bnt_all_choose)

    def page_settle(self):
        self.base_click(page.order_bnt_settle)

    def page_submit(self):
        self.base_click(page.order_bnt_submit)

    def page_input_purchase_password(self, value):
        self.base_input(page.order_purchase_password, value)

    def page_btn_password(self):
        self.base_click(page.order_bnt_sure)

    def page_order(self, purchase_password):
        self.page_btn_all_choose()
        self.page_settle()
        sleep(5)
        self.page_submit()
        self.page_input_purchase_password(purchase_password)
        self.page_btn_password()

