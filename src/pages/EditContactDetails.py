from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import time
class EditContactDetails(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    locators = {
        "edit_contact_details" : (By.ID, "ContentPlaceHolder1_hlEditContact" ),
        "aemail" : (By.ID,"ContentPlaceHolder1_tbAlterEmail" ),
        "address" : (By.ID, "ContentPlaceHolder1_tbPACity"),
        "save" : (By.ID,"ContentPlaceHolder1_btnSubmit" )
    }
    def click_edit_contact_details(self):
        self.edit_contact_details.click()
    def aemail(self,aemail):
        self.altemail.send_keys(aemail)
    def address(self,address):
        self.address.send_keys(address)
    def save(self):
        self.save.click()
