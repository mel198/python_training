from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.test_modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_header_name(app):
    app.session.login(username="admin", password="secret")
    app.group.test_modify_first_group(Group(header="New header"))
    app.session.logout()


def test_modify_footer_name(app):
    app.session.login(username="admin", password="secret")
    app.group.test_modify_first_group(Group(header="New footer"))
    app.session.logout()


