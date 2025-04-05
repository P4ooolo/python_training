# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_number(app, data_contacts):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_form()
    app.contact.create_contact(data_contacts)
    app.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(data_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

