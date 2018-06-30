# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_3(app):
    app.group.create(Group(name="wer", header="cbv", footer="fgj"))


def test_add_empty_group_3(app):
    app.group.create(Group(name="", header="", footer=""))

