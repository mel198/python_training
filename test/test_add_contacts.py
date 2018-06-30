# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contacts_2(app):
    app.contact.create(Contact(name="Ro", midname="N", lastname="Vi", nickname="me", company="bel"))


def test_add_contacts_empty(app):
    app.contact.create(Contact("", "", "", "", ""))

