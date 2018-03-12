# -*- coding: UTF-8 -*-
# python F:\py\project02\testCase\pageObj\basePage.py

import common.plog as Log
import common.pathcfg as pathcfg
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *

log = Log.MyLog.get_log()
logger = log.get_logger()

class Page:
    '''
    页面基础类
    '''
    def __init__(self, selenium_driver):
        #self.base_url = bbs_url
        self.driver = selenium_driver
        self.timeout = 10
        self.imgPath = pathcfg.imagePathToday

    def get(self, url, title=''):
        '''打开网页，可选择判断title是否符合预期'''
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        except TimeoutException as e1:
            logger.error('打开网页超时，原因是：%s' % e1)
        except Exception as e2:
            logger.error('打开网页失败，原因是：%s' % e2)

    def find_element(self, loc, timeout=10):
        '''查找单个元素，并显式等待，默认10秒'''
        element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(loc))
        return element
        
    def find_elements(self, loc, timeout=10):
        '''查找多个元素'''
        elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(loc))
        return elements

    def click(self, loc):
        '''点击'''
        element = self.driver.find_element(*loc)
        element.click()

    def send_keys(self, text):
        '''清空并输入文本'''
        element = self.driver.find_element(*loc)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, loc, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(loc, text))
        except TimeoutException as e:
            logger.error('元素等待超时，%s' % e)
            return False
        else:
            return result

    def is_text_in_value(self, loc, text, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(loc, text))
        except TimeoutException as e:
            logger.error('元素等待超时，%s' % e)
            return False
        else:
            return result

    def is_title(self, text, timeout=10):
        '''判断当前页面的title是否等于text'''
        result = WebDriverWait(self.driver, timeout).until(EC.title_is(text))
        return  result

    def is_title_contains(self, text, timeout=10):
        '''判断当前页面的title是否包含text'''
        result = WebDriverWait(self.driver, timeout).until(EC.title_contains(text))
        return  result

    def is_selected(self, loc, timeout=10):
        '''判断元素是否被选中，返回bool'''
        result = WebDriverWait(self.driver, timeout).until(EC.element_located_to_be_selected(loc))
        return  result

    def is_selected_be(self, loc, state=True, timeout=10):
        '''元素的被选中状态，与预期True/False一致返回返回True，不一致返回False'''
        result = WebDriverWait(self.driver, timeout).until(EC.element_located_selection_state_to_be(loc, state))
        return  result

    def is_alert_present(self, timeout=10):
        '''有alert返回alert，没有返回False'''
        result = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        return result

    def is_visibility(self, loc, timeout=10):
        '''元素可见返回element，否则返回False'''
        result = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
        return result

    def is_invisibility(self, loc, timeout=10):
        '''元素不可见返回True，没找到元素返回True，可见返回element'''
        result = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(loc))
        return result

    def is_clickable(self, loc, timeout=10):
        '''元素可点击返回element，不可点击返回False'''
        result = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(loc))
        return result

    def is_located(self, loc, timeout=10):
        '''元素可定位返回element，不可点击返回False'''
        result = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(loc))
        return result

    def script(self, src):
        '''执行js脚本'''
        return self.driver.execute_script(src)

    def move_to_element(self, loc):
        '''鼠标移动到指定位置悬停'''
        element = self.driver.find_element(*loc)
        ActionChains(self.driver.move_to_element(element)).perform()

    def get_title(self):
        '''返回当前页面title'''
        return self.driver.title

    def get_text(self, loc):
        '''返回元素text'''
        element = self.driver.find_element(*loc)
        return element.text

    def get_attribute(self, loc, name):
        '''返回元素属性'''
        element = self.driver.find_element(*loc)
        return element.get_attribute(name)

    def js_fous_element(self, loc):
        '''聚焦元素'''
        target = self.driver.find_element(*loc)
        self.driver.execute_script('arguments[0].scrollIntoView();', target)

    def js_scoll_top(self):
        '''滚动到顶部'''
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scoll_end(self):
        '''滚动到底部'''
        js = 'window.scrollTo(0,document.body.scroolHeight)'
        self.driver.execute_script(js)

    def select_by_index(self, loc, index):
        '''通过索引定位select下拉框，索引从0开始'''
        element = self.driver.find_element(*loc)
        Select(element).select_by_index(index)

    def select_by_value(self, loc, value):
        '''通过value定位select下拉框'''
        element = self.driver.find_element(*loc)
        Select(element).select_by_value(value)

    def select_by_text(self, loc, text):
        '''通过可见文本定位select下拉框'''
        element = self.driver.find_element(*loc)
        Select(element).select_by_visible_text(text)

    def get_screenshot(self, imgName='截图'):
        '''截图'''
        nowtime = datetime.now().strftime('%Y%m%d%H%M%S')
        logger.info("保存截图成功，路径为%s" % self.imgPath + os.sep + imgName + nowtime + ".png")
        self.driver.get_screenshot_as_file(self.imgPath + os.sep + imgName + nowtime + ".png")
            #self.driver.get_screenshot_as_file(self.imgPath + os.sep + ospicName)
            #self.logger.info("执行用例%s，保存截图成功，路径为%s。" % (caseName, imgName))
        #except Exception as e:
            #self.logger.error("截图失败，原因是：%s" % e, exc_info=True)

    def to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def forword(self):
        '''前进'''
        self.driver.forword()

    def back(self):
        '''后退'''
        self.driver.back()

    def quit(self):
        '''关闭浏览器，清空临时文件'''
        self.driver.quit()

    def close(self):
        '''关闭当前页面'''
        self.driver.close()


class Screen(object):
    '''截图装饰器'''
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                nowTime = pathcfg.nowTime
                imgFile = os.path.join(pathcfg.imagePathToday, '异常%s.png' % nowTime)
                self.driver.get_screenshot_as_file(imgFile)
                raise
        return inner


