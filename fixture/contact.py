from selenium.webdriver.support.ui import Select

class contactHelper:

    def __init__(self, app):
        self.app = app

    def open_form(self):
            wd = self.app.wd
            wd.find_element_by_link_text("add new").click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def create_contact(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.get("http://p4ooolo.local/addressbook/edit.php")
        self.fill_contact_form(contact)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("middlename", contact.middlename)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nickname)
        self.change_contact_value("title", contact.title)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("homenumber", contact.homenumber)
        self.change_contact_value("mobile", contact.mobile)
        self.change_contact_value("work", contact.work)
        self.change_contact_value("fax", contact.fax)
        self.change_contact_value("email", contact.email)
        self.change_contact_value("email2", contact.email2)
        self.change_contact_value("bday", contact.bday)
        self.change_contact_value("homepage", contact.homepage)
        self.change_contact_value("email3", contact.email3)
        self.change_contact_value("bmonth", contact.bmonth)
        self.change_contact_value("byear", contact.byear)
        self.change_contact_value("aday", contact.aday)
        self.change_contact_value("amonth", contact.amonth)
        self.change_contact_value("ayear", contact.ayear)


    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # open modification form
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def delete_first_number(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//input[@value="Delete"]')

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/div/i/a").click()

