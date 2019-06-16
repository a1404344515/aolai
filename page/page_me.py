from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    a=By.ID,'com.yunmall.lc:id/tv_user_nikename'
    def get_id(self):
        self.get_text(self.a)