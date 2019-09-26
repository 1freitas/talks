import os
from time import sleep

import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
os.path.join(os.path.dirname(__file__), p)
)

PLATFORM_VERSION = '7.0' #API24
#PLATFORM_VERSION = '9' #API28
#DEVICE_NAME = 'sdk_google_phone_x86'
#DEVICE_NAME = 'sdk_gphone_x86_64'
DEVICE_NAME='sdk_google_phone_x86'

class SimpleAndroidTests(unittest.TestCase):

  def setUp(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = PLATFORM_VERSION
    desired_caps['deviceName'] = DEVICE_NAME
    desired_caps['autoGrantPermissions'] = 'true'       
    desired_caps['appPackage'] = 'com.example.teste_flutter'
    desired_caps['appActivity'] = '.MainActivity' #home
    desired_caps['noReset'] = 'true'
    desired_caps['fullReset'] = 'false'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

  def tearDown(self):
    # end the session
    self.driver.quit()

  def test_keyboard(self): 
    sleep(3)
    # inserir texto
    texto = self.driver.find_elements_by_class_name('android.widget.EditText')
    print("TEXTO", texto[0].is_enabled)
    texto[0].click()
    els4 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
    for i in range(len(els4)):
      if ('Aplicar' in els4[i].text):
        els4[i].click()
        break
    sleep(1)

  def test_finds(self):
    els = self.driver.find_elements_by_android_uiautomator("new UiSelector().enabled(true)")   
    for i in range(len(els)):
      print("ELS ENABLED",i,els[i].text)		
    els2 = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")   
    for i in range(len(els2)):
      print("ELS 2 CLICKABLED",i,els2[i].text)
		
  def test_input(self): 
    sleep(3)	
    els3 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
    for i in range(len(els3)):		
      if ('Limpar' in els3[i].text):
        els3[i].click()
        break
    sleep(2)
    els4 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.EditText")')
    for i in range(len(els4)):		
      if ('App' in els4[i].text):
        print(els4[i].text)
        els4[i].send_keys('Abacaxi')	
        break		
    els5 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
    for i in range(len(els5)):		
      if ('Aplicar' in els5[i].text):
       els5[i].click()
       break
  
if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
  unittest.TextTestRunner(verbosity=3).run(suite)
