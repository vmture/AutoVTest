# -*- coding: utf-8 -*-
__author__ = 'vmture'
# from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import pymysql
import re

class Search_Ticket:
    def __init__(self):
        SHA = 'SHA'
        SHA_NUM = '%C9%CF%BA%A3'
        SZX = 'SZX'
        SZX_NUM = '%C9%EE%DB%DA'
        self.SHA_SZX_URL = []
        self.Date = ['2016-08-10', '2016-08-11', '2016-08-12']
        for i in self.Date:
            self.SHA_SZX_URL.append(
                'https://sjipiao.alitrip.com/flight_search_result.htm?spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=' + SZX_NUM + '&depCity=' + SZX + '&depDate=' + i + '&arrCityName=' + SHA_NUM + '&arrCity=' + SHA + '&arrDate=')

    def SHA_SZX(self):
        # SHA_SZX_URL=[
        # 'https://sjipiao.alitrip.com/flight_search_result.htm?spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=%C9%CF%BA%A3&depCity=SHA&depDate=2016-09-06&arrCityName=%C9%EE%DB%DA&arrCity=SZX&arrDate=']
        # # 'http://flights.ctrip.com/booking/SHA-SZX-day-1.html?DDate1=2016-09-10',
        #     # 'http://flights.ctrip.com/booking/SHA-SZX-day-1.html?DDate1=2016-09-11']
        PlaneCompany = []
        Beign_time = []
        Arrive_time = []
        Beign_Place = []
        Arrive_Place = []
        Ticket_fee = []
        Plane_line = []
        for url in self.SHA_SZX_URL:
            # service_args = ['--proxy=localhost:9999', '--proxy-type=socks5', ]
            # driver =webdriver.PhantomJS(executable_path="phantomjs.exe",service_args=service_args)
            # driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(url)
            date = re.findall(r'\d+\-\d+-\d+',url)
            # sleep(2)
            # button = driver.find_element_by_id('ks-overlay-close-ks-component1015')
            # button.click()
            sleep(10)
            html = driver.page_source
            driver.get_screenshot_as_file(date[0]+'WebPage.jpg')
            driver.quit()
            bs_obj = BeautifulSoup(html, 'html.parser')
            # print(bs_obj)

            for line in bs_obj.find_all('h3',{'class':'search-msg'}):
                Plane_line.append(line.get_text())
            for i in bs_obj.find_all('td', {'class': 'flight-line'}):
                PlaneCompany.append(i.get_text())
            for j in bs_obj.find_all('p', {'class': 'flight-time-deptime'}):
                Beign_time.append(j.get_text())
            for k in bs_obj.find_all('span', {'class': 's-time'}):
                Arrive_time.append(k.get_text())
            for l in bs_obj.find_all('p', {'class': 'port-dep'}):
                Beign_Place.append(l.get_text())
            for m in bs_obj.find_all('p', {'class': 'port-arr'}):
                Arrive_Place.append(m.get_text())
            for n in bs_obj.find_all('td', {'class': 'flight-price J_FlightPriceWrap'}):
                Ticket_fee.append(n.get_text())
            # print(Beign_time)
            # print(Arrive_time)
            # try:
            #     print('SZX  ---->  SHA  ' + self.Date[num] + ': \n')
            #     num += 1
            # except:
            #     pass
                # for num in range(len(PlaneCompany)):
                #     print(u'航班:  ' + PlaneCompany[num])
                #     print(u'起飞时间:  ' + Beign_time[num])
                #     print(u'降落时间:  ' + Arrive_time[num])
                #     print(u'起飞地点:  ' + Beign_Place[num])
                #     print(u'降落地点:  ' + Arrive_Place[num])
                #     print(u'票价:  ' + Ticket_fee[num] + '\n')
        Ticket_db = pymysql.connect('localhost', 'root', '', 'test')
        cursor = Ticket_db.cursor()
        Ticket_dba = cursor.execute("SHOW TABLES LIKE 'PLANE_TICKET'")
        if Ticket_dba == 0:
            Create_db = '''
            CREATE TABLE PLANE_TICKET (
            PlANE  CHAR(40) NOT NULL,
            PLANE_LINE CHAR (20) NOT NULL PRIMARY KEY ,
            BEGIN_TIME CHAR(20),
            ARRIVE_TIME CHAR(20),
            BEGIN_PLACE CHAR(20),
            ARRIVE_PLACE CHAR(20),
            TICKET_FEE CHAR(20) )
            '''
            cursor.execute(Create_db)
        try:
            for num in range(len(Search_Ticket.SHA_SZX().PlaneCompany)):
                insert_data = """ INSERT INTO PLANE_TICKET(PLANE, PLANE_LINE, BEGIN_TIME, ARRIVE_TIME, BEGIN_PLACE, ARRIVE_PLACE, TICKET_FEE)
                              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % \
                              (PlaneCompany[num],
                               Plane_line[num],
                               Beign_time[num],
                               Arrive_time[num],
                               Beign_Place[num],
                               Arrive_Place[num],
                               Ticket_fee[num])
                try:
                    cursor.execute(insert_data)
                    cursor.commit()
                except:
                    cursor.rollback()
        except:
            pass
        cursor.close()

    def TicketC_db(self):

        Ticket_db = pymysql.connect('localhost', 'root', '', 'test')
        cursor = Ticket_db.cursor()
        Ticket_dba = cursor.execute("SHOW TABLES LIKE 'PLANE_TICKET'")
        if Ticket_dba == 0:
            Create_db = '''
            CREATE TABLE PLANE_TICKET (
            PlANE  CHAR(40) NOT NULL,
            PLANE_LINE CHAR (20) NOT NULL PRIMARY KEY ,
            BEGIN_TIME CHAR(20),
            ARRIVE_TIME CHAR(20),
            BEGIN_PLACE CHAR(20),
            ARRIVE_PLACE CHAR(20),
            TICKET_FEE CHAR(20) )
            '''
            cursor.execute(Create_db)
        Ticket_db.close()

    def Insert_data(self):
        Ticket_db = pymysql.connect('localhost', 'root', '', 'test')
        cursor = Ticket_db.cursor()
        try:
            for num in range(len(Search_Ticket.SHA_SZX().PlaneCompany)):
                insert_data = """ INSERT INTO PLANE_TICKET(PLANE, PLANE_LINE, BEGIN_TIME, ARRIVE_TIME, BEGIN_PLACE, ARRIVE_PLACE, TICKET_FEE)
                              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % \
                              (Search_Ticket.SHA_SZX().PlaneCompany[num],
                               Search_Ticket.SHA_SZX().Plane_line[num],
                               Search_Ticket.SHA_SZX().Beign_time[num],
                               Search_Ticket.SHA_SZX().Arrive_time[num],
                               Search_Ticket.SHA_SZX().Beign_Place[num],
                               Search_Ticket.SHA_SZX().Arrive_Place[num],
                               Search_Ticket.SHA_SZX().Ticket_fee[num])
                try:
                    cursor.execute(insert_data)
                    cursor.commit()
                except:
                    cursor.rollback()
        except:
            pass
        cursor.close()


if __name__ == '__main__':
    self = Search_Ticket()
    self.__init__()
    self.SHA_SZX()
    # self.TicketC_db()
    # self.Insert_data()