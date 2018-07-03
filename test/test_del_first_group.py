from model.group import Group


def test_del_group(app):
    app.open_home_page()
    app.group.open_group_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.test_del_first_group()
    app.group.return_to_group_page()


