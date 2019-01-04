from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url, secret_password):
        if browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.secret_password = secret_password
#        self.wd.maximize_window()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_login_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_on_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()



