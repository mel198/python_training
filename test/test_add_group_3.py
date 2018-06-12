# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group_3(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="wer", header="cbv", footer="fgj"))
    app.logout()


def test_test_add_empty_group_3(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

