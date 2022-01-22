class loginpageobjs():

    def __init__(self,driver):
        self.driver = driver

        self.login_username = "txtUsername"
        self.login_password = "txtPassword"
        self.login_btn = "btnLogin"

    def setupusername(self,user):
        self.driver.find_element_by_id(self.login_username).send_keys(user)

    def setuppassword(self,password):
        self.driver.find_element_by_id(self.login_password).send_keys(password)

    def clickonloginbtn(self):
        self.driver.find_element_by_id(self.login_btn).click()

