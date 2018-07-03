from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Romtest", midname="Nitest", lastname="Vistest", nickname="mytest", company="beldtest"))
    app.contact.test_modify_first_contact(Contact(name="Rom", midname="Ni", lastname="Vis", nickname="my", company="beld"))


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="", midname="", lastname="", nickname="", company=""))
    app.contact.test_modify_first_contact(Contact(name="Rom", midname="Ni", lastname="Vis", nickname="my", company="beld"))