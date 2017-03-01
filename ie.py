from selenium import webdriver
from time import sleep
import os

if __name__ == '__main__':

    caps = {}
    caps['browserName'] = 'internet explorer'
    port = 4444
    driver = webdriver.Remote(
        desired_capabilities=caps,
        command_executor="http://127.0.0.1:%s/wd/hub" % (port)        
    )
    driver.implicitly_wait(30)
    driver.get('http://google.com')
    sleep(5)
    print "Title:"
    print driver.title
    driver.quit()

    print "Done"
