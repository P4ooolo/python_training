# -*- coding: utf-8 -*-
def test_delete_first_number(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_number()
    app.return_to_home_page()
    app.session.logout()