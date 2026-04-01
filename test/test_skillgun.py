from selenium import webdriver
import time
from src.pages.SkillgunMainPage import SkillgunMainPage
from src.pages.Skillgundashboard import SkillgunDashBoard
from src.pages.SkillgunPlacementPage import SkillgunPlacementPage
from src.pages.SkillgunProfileSetting import SkillgunProfileSetting
from src.pages.EditContactDetails import EditContactDetails
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
def test_skillgun_login():
    driver.get("http://skillgun.com")
    time.sleep(5)
    s = SkillgunMainPage(driver)
    s.enter_mobile("9902315354")
    time.sleep(5)
    s.enter_email("prashantnagure00@gmail.com")
    time.sleep(5)
    s.enter_password("Nagure@1234")
    time.sleep(5)
    s.cb.click()
    time.sleep(5)
    s.log.click()
    time.sleep(5)
    assert 'Home' in driver.current_url
def test_skillgun_dashboard():
    d = SkillgunDashBoard(driver)
    d.interview.click()
    d.gotohome.click()
    time.sleep(5)
    assert 'Home' in driver.current_url
def test_skillgun_placement_page():
    p =SkillgunPlacementPage(driver)
    p.new_placements_drive.click()
    p.gotohome1.click()
    time.sleep(5)
    assert 'Home' in driver.current_url
def test_skillgun_profile_page():
    a = SkillgunProfileSetting(driver)
    a.profile_settings.click()
    time.sleep(5)
    assert 'ProfileSetting' in driver.current_url
def test_edit_contact_details_page():
    e = EditContactDetails(driver)
    e.edit_contact_details.click()
    time.sleep(5)
    e.aemail("prashantnagure00@gmail.com")
    time.sleep(5)
    e.address("aland")
    time.sleep(5)
    e.save.click()
    time.sleep(5)
    assert 'Contact Details Updated Successfully' in driver.current_url


