__author__ = 'vmture'
import start
from time import sleep
import device
# device.Testdevice=raw_input()
# print device.Testdevice
# device.Testdevice['platformName']
# start.setUp(device.m2note['platformName'],device.m2note['platformVersion'],device.m2note['deviceName'])
driver={'driver':None}
start.setUp(driver)
sleep(5)
start.quit(driver)