class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        # open_contacts_page
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact_add
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.name)
        self.change_field_value("lastname", contact.name)
        self.change_field_value("nickname", contact.name)
        self.change_field_value("company", contact.name)

    def test_select_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # choose check box
        wd.find_element_by_name("selected[]").click()

    def test_del_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # choose check box
        self.test_select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def test_modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        # choose first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact
        self.fill_contact_form(new_contact_data)
        #click submit
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

