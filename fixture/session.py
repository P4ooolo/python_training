class sessionHelper:

    def __init__(self, app):
        self.app = app


    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logget_user() == username


    def get_logget_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()


    def login(self, username, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/index.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()