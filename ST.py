# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\\Selenium Test\\Selenium-Test\\chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=7hgm3O1.jpg")
        time.sleep(2)
        driver.find_element_by_id("uploadImage").clear()
        um = driver.find_element_by_id("uploadImage")
        um.send_keys("D:\\Selenium Test\\Selenium-Test\\7hgm3O1.jpg")
        time.sleep(2)
        send = driver.find_element_by_xpath("//input[@value='Send']")
        send.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
