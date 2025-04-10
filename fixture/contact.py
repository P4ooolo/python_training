from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
import time


class contactHelper:

    def __init__(self, app):
        self.app = app

    def open_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def select_first_contact(self):
        self.select_contact_by_index(0)


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def create_contact(self, contact):
        # init contact creation
        self.open_form()
        self.fill_contact_form(contact)
        self.submit_new_number()
        self.contact_cache = None


    def fill_contact_form(self, contact):
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("middlename", contact.middlename)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nickname)
        self.change_contact_value("title", contact.title)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("home", contact.homenumber)
        self.change_contact_value("mobile", contact.mobile)
        self.change_contact_value("work", contact.work)
        self.change_contact_value("fax", contact.fax)
        self.change_contact_value("email", contact.email)
        self.change_contact_value("email2", contact.email2)
        self.change_select_value("bday", contact.bday)
        self.change_contact_value("homepage", contact.homepage)
        self.change_contact_value("email3", contact.email3)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_contact_value("byear", contact.byear)
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_contact_value("ayear", contact.ayear)


    def submit_new_number(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()


    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # open modification form
        wd.find_element_by_css_selector('tr[name="entry"] td:nth-child(8) a').click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # open modification form
        wd.find_element_by_css_selector(f'tr:nth-child({index+2}) td:nth-child(8) a').click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        # open modification form
        wd.find_element_by_css_selector(f'a[href="edit.php?id={id}"]').click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def delete_first_number(self):
        self.delete_number_by_index(0)


    def delete_number_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.contact_cache = None


    def delete_number_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('table tr[name="entry"]'):
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)


    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homenumber = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homenumber=homenumber, work=work, mobile=mobile,
                       email=email, email2=email2, email3=email3, address=address)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homenumber = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        # fax = re.search("F: (.*)", text).group(1)
        return Contact(homenumber=homenumber, work=work, mobile=mobile)


    def select_group_on_home_page(self):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        selected_first_group = wd.find_element_by_css_selector("select[name='to_group'] option:nth-child(1)")
        selected_first_group.click()
        return selected_first_group.get_attribute('value')


    def select_group_on_home_page_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_css_selector("select[name='to_group'] option[value='%s']" % group_id).click()


    def filter_contacts_by_group_id(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        wd.find_element_by_css_selector("select[name='group'] option[value='%s']" % group_id).click()


    def click_add_to_group(self):
        wd = self.app.wd
        wd.find_element_by_name("add").click()


    def click_remove_from_group(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()


    def get_first_contact_id(self):
        wd = self.app.wd
        return wd.find_elements_by_name("selected[]")[0].get_attribute("value")