#-*- coding: utf-8 -*-
__author__ = 'vmture'
# from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
class Search_Ticket:
    def SHA_SZX(self):
        SHA_SZX_URL=[
            'https://sjipiao.alitrip.com/flight_search_result.htm?spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=%C9%CF%BA%A3&depCity=SHA&depDate=2016-09-06&arrCityName=%C9%EE%DB%DA&arrCity=SZX&arrDate=']
            # 'http://flights.ctrip.com/booking/SHA-SZX-day-1.html?DDate1=2016-09-10',
            # 'http://flights.ctrip.com/booking/SHA-SZX-day-1.html?DDate1=2016-09-11']

        for url in SHA_SZX_URL:
            service_args = ['--proxy=localhost:9999', '--proxy-type=socks5', ]
            driver =webdriver.PhantomJS(executable_path="phantomjs.exe",service_args=service_args)
            # driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
            # driver = webdriver.Chrome()
            # driver.maximize_window()
            driver.get(url)
            # sleep(2)
            # button = driver.find_element_by_id('ks-overlay-close-ks-component1015')
            # button.click()
            sleep(10)
            html = driver.page_source
            driver.get_screenshot_as_file('WebPage.jpg')
            driver.quit()
            bs_obj = BeautifulSoup(html, 'html.parser')
            # print(bs_obj)

            PlaneCompany = []
            Beign_time = []
            Arrive_time = []
            Beign_Place = []
            Arrive_Place = []
            Ticket_fee = []

            for i in bs_obj.find_all('td', {'class':'flight-line'}):
                PlaneCompany.append(i.get_text())
            for j in bs_obj.find_all('p', {'class':'flight-time-deptime'}):
                Beign_time.append(j.get_text())
            for k in bs_obj.find_all('span', {'class':'s-time'}):
                Arrive_time.append(k.get_text())
            for l in bs_obj.find_all('p', {'class':'port-dep'}):
                Beign_Place.append(l.get_text())
            for m in bs_obj.find_all('p', {'class':'port-arr'}):
                Arrive_Place.append(m.get_text())
            for n in bs_obj.find_all('td', {'class':'flight-price J_FlightPriceWrap'}):
                Ticket_fee.append(n.get_text())
            # print(Beign_time)
            # print(Arrive_time)
            for num in range(len(PlaneCompany)):
                print(u'航班:  ' + PlaneCompany[num])
                print(u'起飞时间:  '+ Beign_time[num])
                print(u'降落时间:  '+ Arrive_time[num])
                print(u'起飞地点:  '+ Beign_Place[num])
                print(u'降落地点:  '+ Arrive_Place[num])
                print(u'票价:  '+ Ticket_fee[num] + '\n')


if __name__ == '__main__':
    self = Search_Ticket()
    self.SHA_SZX()