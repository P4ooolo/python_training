import re

def test_phones_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    for contact in contacts_from_home_page:
        db_contact = db.get_contact_by_id(contact.id)
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(db_contact)
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(db_contact)
        assert contact.firstname == db_contact.firstname.strip()
        assert contact.lastname == db_contact.lastname.strip()
        assert contact.address == db_contact.address.strip()
        print(db_contact)


def clear(s):
    return re.sub("[(). -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homenumber, contact.mobile, contact.work]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: x.strip(), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))