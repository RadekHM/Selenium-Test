# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re


class Incorrect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\\Selenium Test\\Selenium-Test\\Files\\chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_incorrect(self):
        driver = self.driver
        driver.get(
            "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=exams.jpg")
        self.assertTrue("media", driver.current_url)
        time.sleep(2)
        el = driver.find_element_by_id("uploadImage")
        time.sleep(2)
        el.send_keys("D:\\Selenium Test\\Selenium-Test\\Files\\search.txt")
        time.sleep(2)
        self.assertEqual("You must select a valid image file!", self.close_alert_and_get_its_text())
        driver.save_screenshot("D:\\Selenium Test\\Selenium-Test\\ScreenShots\\Unsucsesfull Test.png")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='Send']").click()

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "_main_":
    unittest.main()
