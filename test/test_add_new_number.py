# -*- coding: utf-8 -*-
from model.contact import Contact
    
def test_add_new_number(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_form()
    contact = Contact(firstname="Ksy", middlename="LOP", lastname="lop", nickname="p4oolo", title="title",
                      company="cft", address="ivanova 8", homenumber="8903678909", mobile="8907543226",
                      work="test", fax="fax", email="hjbhgc@ghff.hgf", email2="jhhfdd@nhv.jhhf", bday="2",
                      homepage="home", email3="hgfgfdfd@bvcv.hgg",
                      bmonth="February", byear="1999", aday="3", amonth="February", ayear="2345")
    app.contact.create_contact(contact)
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

