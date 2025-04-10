from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.create(Group(name="test"))
    app.return_to_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    if db.is_contact_in_group(contact.id, group.id):
        app.contact.filter_contacts_by_group_id(group.id)
        app.contact.select_contact_by_id(contact.id)
        app.contact.click_remove_from_group()
    app.return_to_home_page()
    app.contact.select_contact_by_id(contact.id)
    app.contact.select_group_on_home_page_by_id(group.id)
    old_count = db.get_contact_count_by_group_id(group.id)
    app.contact.click_add_to_group()
    new_count = db.get_contact_count_by_group_id(group.id)
    assert old_count + 1 == new_count

def test_del_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    if db.get_contact_count_by_group_id(group.id) == 0:
        app.return_to_home_page()
        app.contact.select_first_contact()
        app.contact.select_group_on_home_page_by_id(group.id)
        app.contact.click_add_to_group()
    app.return_to_home_page()
    app.contact.filter_contacts_by_group_id(group.id)
    old_count = db.get_contact_count_by_group_id(group.id)
    app.contact.select_first_contact()
    app.contact.click_remove_from_group()
    new_count = db.get_contact_count_by_group_id(group.id)
    assert old_count - 1 == new_count




