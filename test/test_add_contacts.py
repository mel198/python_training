# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contacts_2(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact("Ro", "N", "Vi", "me", "bel"))
    app.session.logout()


def test_add_contacts_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact("", "", "", "", ""))
    app.session.logout()

