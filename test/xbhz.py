"""
==========================
Author   : 文闯
Time     : 2022/07/16 20:59
FileName : xbhz.py
Company  : 功夫豆
==========================
"""
import time
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
# 1.设置终端参数项
desired_caps={
    "platformName":"android",
    "platformVersion":"10",
    "deviceName":"2XT0218A22023206",
    "appPackage":"com.xbxxhz.box",
    "appActivity":"com.xbxxhz.box.FlashAct",
    "automationName": "UIAutomator2"
}
# 发送指令给appium server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# 获取屏幕尺寸

Windows_size = driver.get_window_size()
print("手机屏幕尺寸：",Windows_size)
x = Windows_size["width"]
y = Windows_size["height"]
# 左滑
# move_to里的坐标是相对于前一个坐标的偏移量
# 将动作命令发送至服务器来执行该动作，如：
action = driver.swipe(start_x=x * 0.95, start_y=y * 0.5,end_x=x * 0.1,end_y=y * 0.5)
# 执行滑动操作
print("执行")
print('左滑')
# 将动作命令发送至服务器来执行该动作，如：
sleep(1)
action1 = driver.swipe(start_x=x * 0.95, start_y=y * 0.5,end_x=x * 0.1,end_y=y * 0.5)
# 执行滑动操作
print("执行1")
print('左滑1')
# 将动作命令发送至服务器来执行该动作，如：
sleep(1)
action2 = TouchAction(driver).press(x=x * 0.95, y=y * 0.5).move_to(x=x * 0.1, y=y * 0.5).release()
# 执行滑动操作
print("执行1")
action2.perform()
print('左滑1')
# for i in range(3):
#     # 将动作命令发送至服务器来执行该动作，如：
#     action = TouchAction(driver).press(x=x * 0.8, y=y * 0.5).move_to(x=x * 0.1, y=y * 0.5).release()
#     # 执行滑动操作
#     print("执行")
#     action.perform()
#     print('左滑')
#点击开始体验按钮
print("开始延时3秒")
sleep(3)
print("3秒结束")
el_tiyan = driver.find_element(By.XPATH, "//*[@resource-id='com.xbxxhz.box:id/lg_navact_item_btn_goHome']")
print(el_tiyan.text)
el_tiyan.click()
sleep(1)
#点击同意按钮
el_tongyi = driver.find_element(By.XPATH, "//*[@resource-id='com.xbxxhz.box:id/view_icon_text_layout_text']")
print(el_tongyi.text)
el_tongyi.click()
sleep(1)
#点击始终允许
el_shizhongyuxu = driver.find_element(By.XPATH, "//*[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
print(el_shizhongyuxu.text)
el_shizhongyuxu.click()
sleep(1)
# 点击微信登录授权
el_weixin = driver.find_element(By.XPATH , "//*[@resource-id='com.xbxxhz.box:id/lg_pre_login_act_wechat']")
print(el_weixin.text)
el_weixin.click()
sleep(1)
# 选择一个微信
el_ClickWechat = driver.find_element(By.XPATH,"//android.widget.GridView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
# el_ClickWechat = driver.tap(x= x*0.289,y=y*0.815,duration=1000)
print(el_ClickWechat.text)
el_ClickWechat.click()
time.sleep(3)
#点击跳过
el_Skip = driver.find_element(By.XPATH, "//*[@text='跳过']")
print(el_Skip.text)
el_Skip.click()
sleep(1)
#点击稍后领取
el_lingqu = driver.find_element(By.XPATH, "//*[@resource-id='com.xbxxhz.box:id/dlg_gfdtipdialog_cancle']")
print(el_lingqu.text)
el_lingqu.click()
time.sleep(2)
#点击取消升级按钮
# el_CancelUpgrade = driver.driver.find_element(By.XPATH,"//*[@resource-id='com.xbxxhz.box:id/dlg_gfdtipdialog_cancle']")
# el_CancelUpgrade.click()
#点击任意空白区域
dianji = driver.tap([(x*0.1, y*0.1)])
time.sleep(5)
driver.quit()
