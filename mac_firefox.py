from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['marionette.logging'] = True

"""
java -client -Xmx256m -Xms20m -Dwebdriver.firefox.logfile=/Users/chef/log/firefox.log -Dwebdriver.server.session.timeout=0 -jar /Volumes/Sauce/selenium/selenium-server-2.53.0.jar -port 4443 -timeout 0

 export VIRTUAL_ENV=/Users/chef/.virtualenvs/sauce
 export PATH="/Volumes/Sauce/Firefox/Firefox 44.app/Contents/MacOS:/Users/chef/.virtualenvs/sauce/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
 export _=/Users/chef/.virtualenvs/sauce/bin/python
 """


driver = webdriver.Remote(
    desired_capabilities=firefox_capabilities,
    command_executor="http://localhost:4443/wd/hub"
)

# driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_binary=firefox_capabilities['binary'],
#                             executable_path='D:\\selenium\\geckodriver.exe')
print driver.desired_capabilities
driver.get('http://theonion.com')

driver.quit()
