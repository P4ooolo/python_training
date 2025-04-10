# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_number(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.create_contact(json_contacts)
    app.return_to_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
