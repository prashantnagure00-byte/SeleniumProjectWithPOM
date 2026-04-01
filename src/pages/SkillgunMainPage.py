from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
class SkillgunMainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    locators = {
         'mobile' : (By.ID,"ContentPlaceHolder1_tbPhoneNumber"),
         'email' : (By.ID,"ContentPlaceHolder1_tbEmail"),
         'password' : (By.ID,"ContentPlaceHolder1_tbPassword"),
         'cb' : (By.XPATH,'//*[@id="ckbkPolicyAgreement"]'),
         'log':(By.ID,"ContentPlaceHolder1_btnLogin")
    }
    def enter_mobile(self, mobile):
        self.mobile.send_keys(mobile)
    def enter_email(self, email):
        self.email.send_keys(email)
    def enter_password(self, password):
        self.password.send_keys(password)
    def enter_cb(self, cb):
        self.cb.click()
    def enter_login(self, log):
        self.login.click()