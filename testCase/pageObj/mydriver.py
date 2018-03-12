# -*- coding: UTF-8 -*-

from selenium import webdriver

import common.plog as Log

log = Log.MyLog.get_log()
logger = log.get_logger()

def browser(browserName = 'firefox'):
    try:
        if browserName == 'chrome':
            driver = webdriver.Chrome()
            logger.info('Chrome浏览器启动')
        elif browserName == 'chrome0':
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            #option.add_argument('--start-maximized')
            option.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(chrome_options=option)
            logger.info('Chrome浏览器以静默模式启动')
        elif browserName == 'firefox':
            driver = webdriver.Firefox()
            logger.info('Firefox浏览器启动')
        elif browserName == 'firefox0':
            option = webdriver.FirefoxOptions()
            option.add_argument('headless')
            option.add_argument('--window-size=1920,1080')
            driver = webdriver.Firefox(firefox_options=option)
            logger.info('Firefox浏览器以静默模式启动')
        else:
            driver = webdriver.Firefox()
            logger.warning('参数错误，默认启动Firefox浏览器')
    except Exception as e:
        logger.error('启动浏览器时出现异常：%s' % e)
    else:
        driver.maximize_window()
        return driver

'''
        if self.browser == 'firefox':
            browser_host = rcf.get_driver('firefox')
            self.driver = Remote(command_executor='http://' + browser_host + '/wd/hub', # 'http://127.0.0.1:4444/wd/hub'
                                 desired_capabilities={'platform':'ANY',
                                                       'browserName': 'firefox', # 'firefox'
                                                       'version':'',
                                                       'javascriptEnabled':True
                                                       }
                                )
        else:
            browser_host = rcf.get_driver('chrome')
            self.driver = Remote(command_executor='http://' + browser_host + '/wd/hub', # 'http://127.0.0.1:4444/wd/hub'
                                 desired_capabilities={'platform':'ANY',
                                                       'browserName': 'chrome', # 'firefox'
                                                       'version':'',
                                                       'javascriptEnabled':True
                                                       }
                                )'''