from selenium import webdriver
from time import sleep
import os

if __name__ == '__main__':

    caps = {}
    caps['browserName'] = 'safari'
    caps['version'] = '10'
    #os.environ["SELENIUM_SERVER_JAR"] = "D:\selenium\selenium-server-2.53.1.jar"
    port = 4444
    driver = webdriver.Remote(
        desired_capabilities=caps,
    #     # command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (user, key)
        command_executor="http://127.0.0.1:%s/wd/hub" % (port)        
    )
    # driver = webdriver.Safari()
    driver.implicitly_wait(30)
    driver.get('http://google.com')
    time.sleep(15)
    driver.quit()

    print "Done"
