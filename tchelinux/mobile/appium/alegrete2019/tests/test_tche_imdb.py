import os
from time import sleep

import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
os.path.join(os.path.dirname(__file__), p)
)

#PLATFORM_VERSION = '7.0'
PLATFORM_VERSION = '9'
#DEVICE_NAME = 'sdk_google_phone_x86'
DEVICE_NAME = 'sdk_gphone_x86_64'

class SimpleAndroidTests(unittest.TestCase):

  def setUp(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = PLATFORM_VERSION
    desired_caps['deviceName'] = DEVICE_NAME
    desired_caps['autoGrantPermissions'] = 'true'
    # causar erro server-side
    #desired_caps['app'] = PATH( '/home/freitas/Documents/Study/TcheLinux/Alegrete2019/com.imdb.mobile.apk')        
    desired_caps['appPackage'] = 'com.imdb.mobile' 
    desired_caps['appActivity'] = '.HomeActivity'
    #desired_caps['appActivity'] = '.login.SigninLoginActivity' # errro
    #desired_caps['appWaitActivity'] = '' 
    #desired_caps['appWaitDuration'] = '30000'
    desired_caps['noReset'] = 'true'
    desired_caps['fullReset'] = 'false'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

  def tearDown(self):
    # end the session
    self.driver.quit()

  def test_login_fail(self): 
	# login fail
	sleep(4)	    
	self.driver.find_element_by_id('com.imdb.mobile:id/menu_account').click()
	#el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "SIGN IN / CREATE ACCOUNT")]')
	self.driver.find_element_by_android_uiautomator('new UiSelector().text("SIGN IN / CREATE ACCOUNT")').click()
	sleep(1)   
	self.driver.find_element_by_id('com.imdb.mobile:id/imdb_auth_portal').click()
	sleep(5) 
	#self.driver.find_element_by_id('com.imdb.mobile:id/apwebview').click()
	els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")   
	for i in range(len(els)):
		#print(els[i].text)
		if (els[i].text == 'Show password'):
			#print("Achei")		
			els[i].click()
	els2 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.EditText")')
	#for i in range(len(els2)):
	#	print("ELS2:", els2[i].tag_name, len(els2))
	els2[0].click()
	#els2[0].send_keys('luana@tchelinux.org')
	els2[0].send_keys('luanadfreitas@gmail.com')
	els2[1].click()
	els2[1].send_keys('abacaxi123')
	sleep(2)
	#self.driver.find_element_by_id('ap_email')
    #self.driver.find_element_by_id('ap_email').click()
	'''self.driver.find_element_by_id('ap_email').send_keys('luana@tchelinux.org')
	sleep(1) 
	self.driver.find_element_by_id('ap_password').send_keys('abacaxi123')'''
	#self.driver.find_element_by_id('signInSubmit').click()
	#sleep(10)
	els3 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
	print("els3", len(els3))
	for i in range(len(els3)):		
		if (els3[i].text == 'Sign-In'):
			print("Achei")
			els[i].click()
			break # se não der break quebra
	sleep(10)
	
	def test_search_starttrek(self): 
	# login pass
	self.driver.find_element_by_id('com.imdb.mobile:id/self_implemented_search').click()
	sleep(1)	
	self.driver.find_element_by_id('com.imdb.mobile:id/search_query').send_keys('Star Treak')


if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
  unittest.TextTestRunner(verbosity=3).run(suite)

#roteiro
'''
emulator -avd Pixel_2_API_28

adb devices -l
List of devices attached
adb server version (41) doesn't match this client (39); killing...
* daemon started successfully
emulator-5554          device product:sdk_gphone_x86_64 model:Android_SDK_built_for_x86_64 device:generic_x86_64 transport_id:1

adb shell
s window windows | grep -E 'mCurrentFocus|mFocusedApp'                        <
  mCurrentFocus=Window{f349c26 u0 com.imdb.mobile/com.imdb.mobile.HomeActivity}
  mFocusedApp=AppWindowToken{a7d809b token=Token{f0cacaa ActivityRecord{1d1d395 u0 com.imdb.mobile/.HomeActivity t8}}}

'''
# freitas:~/Android/Sdk$ adb shell
#adb server version (41) doesn't match this client (39); killing...
#* daemon started successfully
#generic_x86:/ $ dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'     
#  mCurrentFocus=Window{250621b u0 com.imdb.mobile/com.imdb.mobile.login.SigninLoginActivity}
#  mFocusedApp=AppWindowToken{1ef74ff token=Token{e9de41e ActivityRecord{ed83059 u0 com.imdb.mobile/.login.SigninLoginActivity t441}}}
#
#https://kobiton.com/book/chapter-3-understanding-the-desired-capabilities/
# https://developer.android.com/studio/command-line/variables

# device name
#yntesis@luana-freitas:/media/syntesis/1D88-27FC/tchelinux_appium$ adb devices -l
#List of devices attached
#emulator-5554          device product:sdk_gphone_x86 model:Android_SDK_built_for_x86 device:generic_x86 transport_id:1

#syntesis@luana-freitas:/media/syntesis/1D88-27FC/tchelinux_appium$ adb devices -l
#List of devices attached
#adb server version (41) doesn't match this client (39); killing...
#* daemon started successfully
#emulator-5554          device product:sdk_google_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86 transport_id:1
#https://qxf2.com/blog/appium-tutorial-python-physical-device/
