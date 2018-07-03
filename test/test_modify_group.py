from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.test_modify_first_group(Group(name="New group"))


def test_modify_header_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.test_modify_first_group(Group(header="New header"))


def test_modify_footer_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.test_modify_first_group(Group(footer="New footer"))



