from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import time
class SkillgunProfileSetting(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    locators = {
        "profile_settings" : (By.XPATH,'//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[4]/div[3]/a'),

    }
    def click_profile_settings(self):
        self.profile_settings.click()
