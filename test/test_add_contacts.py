# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contacts_2(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("Ro", "N", "Vi", "me", "bel"))
    app.session.logout()


def test_add_contacts_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("", "", "", "", ""))
    app.session.logout()

