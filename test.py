import unittest
from selenium import webdriver
from time import sleep
import os
# import caps

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        user = os.getenv('SAUCE_USERNAME', '')
        key = os.getenv('SAUCE_ACCESS_KEY', '')
        cap = {}

        profile = None

        cap['platform'] = 'Windows 7'
        cap['browserName'] = 'firefox'
        cap['version'] = '32' 
        cap['name'] = 'My test'    
        # cap['tunnelIdentifier'] = os.getenv('TRAVIS_JOB_NUMBER')   

        self.driver = webdriver.Remote(
            desired_capabilities=cap,
            command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (user, key),
        )
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        # self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.driver.get('https://localhost:4443/alert.html')
        # self.driver.get('https://localhost:8000/alert.html')

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()