from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New Name", lastname="Newby")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    app.return_to_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(Contact(firstname="test"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(lastname="New Lastname"))
#     app.return_to_home_page()
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)