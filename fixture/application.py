from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.contact import contactHelper
from fixture.group import groupHelper
from fixture.session import sessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(20)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)
        self.base_url = base_url


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def destroy(self):
        self.wd.quit()


    def return_to_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/index.php"):
            wd.get(self.base_url)