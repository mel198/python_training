from model.contact import Contact


def test_del_contact(app):
    app.open_home_page()
    app.open_contacts_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.test_del_first_contact()
