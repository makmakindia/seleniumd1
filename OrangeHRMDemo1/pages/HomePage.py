class homepageobjs():

    def __init__(self,driver):
        self.driver = driver


        self.welcome_text_link = "welcome"
        self.logout_text_link = "Logout"

    def clik_welcome(self):
        self.driver.find_element_by_id(self.welcome_text_link).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_text_link).click()

