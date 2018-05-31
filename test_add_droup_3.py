# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_droup_3(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},firefox_binary="/Applications/Firefox-ESR.app/Contents/MacOS/firefox")
        self.wd.implicitly_wait(60)

    def test_test_add_group_3(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.init_group_create(wd)
        self.create_group(wd, name="wer", header="cbv", footer="fgj")
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_test_add_group_3(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.init_group_create(wd)
        self.create_group(wd, name="", header="", footer="")
        self.return_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        # return_to_groups_page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, name, header, footer):
        # create group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_name("submit").click()

    def init_group_create(self, wd):
        # init group create
        wd.find_element_by_name("new").click()

    def open_group_page(self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()