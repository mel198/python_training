# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import AppContact


@pytest.fixture
def app(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contacts_2(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact("Ro", "N", "Vi", "me", "bel"))
    app.logout()


def test_add_contacts_empty(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact("", "", "", "", ""))
    app.logout()

