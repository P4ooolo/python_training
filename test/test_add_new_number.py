# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
    
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

testdata = [
    Contact(
        firstname=random_string("firstname", 10),
        middlename=random_string("middlename", 10),
        lastname=random_string("lastname", 10),
        nickname=random_string("nickname", 10),
        title=random_string("title", 10),
        company=random_string("company", 10),
        address=random_string("address", 10),
        homenumber=random_string("homenumber", 10),
        mobile=random_string("mobile", 10),
        work=random_string("work", 10),
        fax=random_string("fax", 10),
        email=random_string("email", 10),
        email2=random_string("email2", 10),
        email3=random_string("email3", 10),
        bday=str(random.randrange(31) + 1),
        homepage=random_string("homepage", 10),
        bmonth=months[random.randrange(len(months) - 1)],
        byear=random_string("byear", 10),
        aday=str(random.randrange(31) + 1),
        amonth=months[random.randrange(len(months) - 1)],
        ayear=random_string("ayear", 10),
    )
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_number(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_form()
    app.contact.create_contact(contact)
    app.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

