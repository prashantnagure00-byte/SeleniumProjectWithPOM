from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import time
class SkillgunDashBoard(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'interview': (By.ID, "ContentPlaceHolder1_ahrefInterview"),
        'gotohome':(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[4]/a'),


    }
    def click_new_placements(self):
        self.new.placements.click()
    def click_interview(self):
        self.interview.click()
        time.sleep(5)
