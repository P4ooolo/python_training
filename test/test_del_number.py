# -*- coding: utf-8 -*-
def test_delete_first_number(app):
    app.contact.delete_first_number()
    app.return_to_home_page()