from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},firefox_binary="/Applications/Firefox-ESR.app/Contents/MacOS/firefox")
        self.wd.implicitly_wait(60)
        self.app = Application
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
       # open home page
        wd.get("http://localhost/addressbook/index.php")

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group create
        wd.find_element_by_name("new").click()
        # create group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        # return_to_groups_page
        wd.find_element_by_link_text("groups").click()

    def destroy (self):
        self.wd.quit()

