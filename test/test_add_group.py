# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_3(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="wer", header="cbv", footer="fgj"))
    app.session.logout()


def test_add_empty_group_3(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

