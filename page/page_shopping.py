from base.base import Base
import page


class PageShopping(Base):
    def page_input_commodity(self, commodity):
        self.base_input(page.shopping_search_box, commodity)

    def page_click_search(self):
        self.base_click(page.shopping_search_btn)

    def page_click_commodity(self):
        self.base_click(page.shopping_commodity_page)

    def page_add_commodity(self):
        self.base_click(page.shopping_add_shopping_cart)

    def page_click_my_cart(self):
        self.base_click(page.shopping_bnt_my_cart)

    def page_shopping(self, commodity):
        self.page_input_commodity(commodity)
        self.page_click_search()
        self.page_click_commodity()
        self.page_add_commodity()
        self.page_click_my_cart()
