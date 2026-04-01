from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import time
class SkillgunPlacementPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'new_placements_drive':(By.ID,"ContentPlaceHolder1_ahrefnewdrive"),
        "gotohome1" : (By.XPATH,'//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[2]/div/a'),

    }
    def click_gotohome(self):
        self.gotohome.click()