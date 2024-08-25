import page
from base.base import Base
from selenium.webdriver.common.action_chains import ActionChains


class PageLogin(Base):
    def page_click_login_link(self):
        self.base_click(page.login_link)

    def page_input_username(self, value):
        self.base_input(page.login_username, value)

    def page_input_password(self, value):
        self.base_input(page.login_password, value)

    def page_click_login_btn(self):
        self.base_click(page.login_bnt)

    def page_get_img(self):
        self.base_get_screenshot()

    def page_sliding(self):
        slider = self.driver.find_element_by_css_selector(page.login_sliding)

        # 使用 ActionChains 模拟拖拽滑动操作
        action = ActionChains(self.driver)
        action.click_and_hold(slider).perform()
        action.move_by_offset(200, 0).perform()  # 假设滑动距离为200，可以根据实际情况调整
        action.release().perform()

    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
        self.page_sliding()
