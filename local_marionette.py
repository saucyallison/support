from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['marionette.logging'] = True
firefox_capabilities['binary'] = 'D:\\Program Files\\Firefox 47\\firefox.exe'

'''
driver = webdriver.Remote(
    desired_capabilities=firefox_capabilities,
    command_executor="http://localhost:4443"
)
'''
driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_binary=firefox_capabilities['binary'],
                            executable_path='D:\\selenium\\geckodriver.exe')
print driver.desired_capabilities
driver.get('http://theonion.com')

driver.quit()