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
    desired_caps['appPackage'] = 'com.imdb.mobile' 
    desired_caps['appActivity'] = '.HomeActivity'
    desired_caps['noReset'] = 'true'
    desired_caps['fullReset'] = 'false'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

  def tearDown(self):
    # end the session
    self.driver.quit()

  def test_search_starttrek(self): 
    sleep(5)
    self.driver.find_element_by_id('com.imdb.mobile:id/search').click()
    sleep(2)	
    self.driver.find_element_by_id('com.imdb.mobile:id/search_src_text').send_keys('Star')
    sleep(3)
    self.driver.press_keycode(66);
    #self.driver.is_keyboard_shown()
    sleep(3)
    #self.driver.back()
    #self.driver.find_elements_by_accessibility_id('Search IMDb').click()
    self.driver.find_element_by_id('com.imdb.mobile:id/search').click()
    self.driver.find_element_by_id('com.imdb.mobile:id/search_src_text').send_keys('star trek')
    sleep(2)
    self.driver.press_keycode(66)	
    sleep(5)
    els = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')
    print("ELS tam:",len(els))
    for i in range(len(els)):
      print("i:", i, els[i].text)
    for i in range(len(els)):
      print("i:", i, els[i].text)
      #if ((els[i].text == "1966-1969  |  TV Series") or (els[i].text == "William Shatner, Leonard Nimoy")):
      if (("TV Series" in els[i].text) or ("Leonard Nimoy" in els[i].text )):
        print("Shazam!!!!")
        els[i].click()
        break
    sleep(3)
    st = self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.imdb.mobile:id/plot_overview")')	
    for i in range(len(st)):
      print("i:", i, st[i].text)		
      self.assertEqual('In the 23rd Century, Captain James T. Kirk and the crew of the USS Enterprise explore the galaxy and defend the United Federation of Planets.', st[i].text) 
      break
    sleep(5)
    self.driver.find_element_by_id('com.imdb.mobile:id/star_your').click()
    sleep(2)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
  unittest.TextTestRunner(verbosity=3).run(suite)


