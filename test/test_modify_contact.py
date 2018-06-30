from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.test_modify_first_contact(Contact(name="Rom"))


def test_modify_contact_midname(app):
    app.contact.test_modify_first_contact(Contact(midname="Ni"))


def test_modify_contact_lastname(app):
    app.contact.test_modify_first_contact(Contact(lastname="Vis"))


def test_modify_contact_nickname(app):
    app.contact.test_modify_first_contact(Contact(nickname="my"))


def test_modify_contact_company(app):
    app.contact.test_modify_first_contact(Contact(company="beld"))

