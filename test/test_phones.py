import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname.strip()
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname.strip()
    assert contact_from_home_page.address == contact_from_edit_page.address.strip()


# def test_phones_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
#     assert contact_from_view_page.homenumber == contact_from_edit_page.homenumber
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.fax == contact_from_edit_page.fax


def clear(s):
    return re.sub("[(). -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homenumber, contact.mobile, contact.work]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: x.strip(), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))