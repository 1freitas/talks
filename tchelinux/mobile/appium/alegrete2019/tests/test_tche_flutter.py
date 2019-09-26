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
		sleep(4)
		# inserir texto
		texto = self.driver.find_elements_by_class_name('android.widget.EditText')
		print("TEXTO", texto[0].is_enabled)	
		els4 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.EditText")')
		for i in range(len(els4)):		
			if ('App' in els4[i].text):
				print(els4[i].text)
				els4[i].click()			
				break	
		self.driver.is_keyboard_shown()
		self.driver.press_keycode(19); #Up
		self.driver.press_keycode(109); #Up
		self.driver.press_keycode(28); #del backspace
		self.driver.press_keycode(67); #del backspace	
		self.driver.press_keycode(28); #del backspace	
		self.driver.press_keycode(115); #Up
		self.driver.press_keycode(48); #T
		self.driver.press_keycode(31); #C
		self.driver.press_keycode(36); #H
		self.driver.press_keycode(33); #E
		self.driver.press_keycode(40); #L
		self.driver.press_keycode(37); #I 	
		self.driver.press_keycode(42); #N
		self.driver.press_keycode(49); #u
		self.driver.press_keycode(52); #X
		self.driver.hide_keyboard()
		els4 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
		for i in range(len(els4)):		
			if ('Aplicar' in els4[i].text):
				els4[i].click()
				break	
		sleep(2)
		
	def test_finds(self):
		sleep(2)
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
				els4[i].click()			
				break	
		self.driver.is_keyboard_shown()
		self.driver.press_keycode(19); #Up
		self.driver.press_keycode(109);
		self.driver.press_keycode(28); 
		self.driver.press_keycode(67); 
		self.driver.press_keycode(28); #del backspace	
		self.driver.press_keycode(115);
		self.driver.press_keycode(48); #T
		self.driver.press_keycode(31); #C
		self.driver.press_keycode(36); #H
		self.driver.press_keycode(33); #E
		self.driver.press_keycode(40); #L
		self.driver.press_keycode(37); #I 	
		self.driver.press_keycode(42); #N
		self.driver.press_keycode(49); #U
		self.driver.press_keycode(52); #X
		self.driver.press_keycode(62); #space
		self.driver.press_keycode(29); #A
		self.driver.press_keycode(40); #L
		self.driver.press_keycode(33); #E
		self.driver.press_keycode(35); #G
		self.driver.press_keycode(46); #R
		self.driver.press_keycode(33); #E
		self.driver.press_keycode(48); #T
		self.driver.press_keycode(33); #E
		self.driver.press_keycode(62); #
		self.driver.press_keycode(62); #
		self.driver.press_keycode(62); #
		self.driver.press_keycode(62); #
		self.driver.press_keycode(62); #
		self.driver.hide_keyboard()
		els4 = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
		for i in range(len(els4)):		
			if ('Aplicar' in els4[i].text):
				els4[i].click()
				break
	
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
	unittest.TextTestRunner(verbosity=3).run(suite)
