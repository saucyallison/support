import unittest
import os
from selenium import webdriver
from time import sleep

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        caps = {}
        true = True
        false = False
        username='awilburfreebiesub3'
        access_key='00e72c6f-bc12-4d66-83f1-fd18c42a62cf'

        caps['platform'] = "Windows 7"
        caps['browserName'] = 'Firefox'
        caps['version'] = '38'
        caps['name'] = username+'\'s test'
        print caps
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://"+username+":"+access_key+"@ondemand.saucelabs.com:80/wd/hub"
        )
        # self.driver.implicitly_wait(30)
        # self.driver.maximize_window()


    def test_mine(self):
        sleep(60)
        # self.driver.get('http://www.google.com')
        # self.driver.execute_script('console.log("console log message from js executor");')
        # self.driver.execute_script("return 2+2;")
        # self.driver.find_element_by_id('loginButton')
        # self.driver.get_screenshot_as_file('screenie.png') 

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()