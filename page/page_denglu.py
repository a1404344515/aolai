from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DengLuPage(BaseAction):
    a=By.ID,'com.yunmall.lc:id/logon_account_textview'
    b=By.ID,'com.yunmall.lc:id/logon_password_textview'
    c=By.ID,'com.yunmall.lc:id/logon_button'
    def input_id(self,id):
        self.input(self.a,id)
    def input_mima(self,mima):
        self.input(self.b,mima)
    def click_denglu(self):
        self.click(self.c)