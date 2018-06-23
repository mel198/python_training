from model.contact import Contact


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(name="Rom"))
    app.session.logout()


def test_modify_contact_midname(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(midname="Ni"))
    app.session.logout()


def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(lastname="Vis"))
    app.session.logout()


def test_modify_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(nickname="my"))
    app.session.logout()


def test_modify_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(company="beld"))
    app.session.logout()

