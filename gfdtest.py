import unittest
import selenium
import time
from appium import webdriver


# super().setUp()
print('selenium version = ', selenium.__version__)
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'UQG0220513008845'
desired_caps['appPackage'] = 'com.xbxxhz.box'
desired_caps["noReset"] = True
desired_caps['appActivity'] = 'com.xbxxhz.box.FlashAct'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# from appium.webdriver.common.appiumby import AppiumBy
#
# # 根据 resource-id 获取元素
# driver.find_element(AppiumBy.ID, 'expand_search')
# # 根据class_name 获取元素
# driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView')
# # 根据 content-desc 属性获取元素
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, '请登录')
# # 根据 xpath 属性获取元素
# driver.find_element(AppiumBy.XPATH, '//ele1/ele2[@attr="value"]')

time.sleep(10)
print("休息了十秒")
driver.quit()


