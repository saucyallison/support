import os
import sys
import httplib
import base64
import json
import new
import unittest
import sauceclient
from selenium import webdriver
from sauceclient import SauceClient
from time import sleep

USERNAME = os.environ.get('SAUCE_USERNAME', '')
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', '')
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = []
for i in range(400):
    browsers.append({'platform':'OS X 10.11', 'browserName':'Safari', 'version':'9', 'idleTimeout':'200', 'build':'Ephox Repro breakpoint'})

def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            # d['desired_capabilities']['build'] = os.environ.get('TRAVIS_JOB_NUMBER')
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


@on_platforms(browsers)
class SauceSampleTest(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()

        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(199)

    def test_sauce(self):
        self.driver.get('http://tbio-testing.s3-website-us-west-2.amazonaws.com/archive/petrie-projects20160203133317/')
        try:
            self.driver.find_element_by_class_name('results')
        except:
            self.driver.execute_script('sauce: break')

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()
