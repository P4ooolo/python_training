# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_number(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.delete_first_number()
    app.return_to_home_page()