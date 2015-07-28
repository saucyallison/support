import unittest
from selenium import webdriver
import os

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        user = os.environ.get('SAUCE_USERNAME')
        key = os.environ.get('SAUCE_ACCESS_KEY')

        caps = {}
        caps['platform'] = 'OS X 10.9'
        caps['version'] = '43'
        caps['browserName'] = 'chrome'
        caps['name'] = 'chrome switches'
        caps['chromeOptions'] = {'args': ['--lang=fr'] }
        
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (user, key),
        )

        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('http://google.com')
        self.driver.execute_script("sauce: break")

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()