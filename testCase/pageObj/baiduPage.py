# -*- coding: UTF-8 -*-
# python F:\py\project02\testCase\pageObj\homePage.py

from testCase.pageObj.basePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from time import sleep
import common.plog as Log

log = Log.MyLog.get_log()
logger = log.get_logger()


class baiduPage(Page):
    '''
    首页
    '''
    search_loc = (By.ID, 'kw')
    search_submit_loc = (By.ID, 'su')

    def to_search(self, keyword):
        '''
        定位到首页的搜索框，输入关键字进行搜索
        '''
        # 清空
        try:
            # 输入关键字
            self.find_element(self.search_loc).send_keys(keyword)
            # 搜索
            self.find_element(self.search_submit_loc).click()
        except TimeoutException as e1:
            logger.error('定位搜索框异常，原因是：%s' % e1)
            raise
        except Exception as e2:
            logger.error('定位搜索框异常，原因是：%s' % e2)
            raise





