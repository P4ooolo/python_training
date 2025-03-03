from model.contact import Contact

def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New Name"))
    app.return_to_home_page()

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New Lastname"))
    app.return_to_home_page()