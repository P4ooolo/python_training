# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_number(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_form()
    app.contact.create_contact(Contact(firstname="Ksy", middlename="LOP", lastname="lop", nickname="p4oolo", title="title", company="cft", address="ivanova 8", homenumber="8903678909", mobile="8907543226",
                            work="test", fax="fax", email="hjbhgc@ghff.hgf", email2="jhhfdd@nhv.jhhf", bday="2", homepage="home", email3="hgfgfdfd@bvcv.hgg",
                            bmonth="February", byear="1999", aday="3", amonth="February", ayear="2345"))
    app.return_to_home_page()
    app.session.logout()
