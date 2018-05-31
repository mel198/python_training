# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="/Applications/Firefox-ESR.app/Contents/MacOS/firefox")
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to group page – возвращаемся на страницу с группами
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd):
        # init group creation (начинаем создавать новую группу)
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        # fill group form (начинаем заполнять форму)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("sdssd")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("sdsd")
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()