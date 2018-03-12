# coding=utf-8
# python F:\py\project02\runAll.py
'''tomorrow、BeautifulReport'''

import os

import unittest
import tomorrow

import readconfig
import common.plog as Log
import common.pemail as Email
import BeautifulReport

import common.pathcfg as pathcfg


# 初始化日志对象
log = Log.MyLog.get_log()
logger = log.get_logger()
# 初始化邮件对象
email = Email.MyEmail.get_email()
# 读取配置文件
rcfg = readconfig.readConfig()

# 路径不存在时自动创建
if not os.path.exists(pathcfg.logPathToday):
    os.makedirs(pathcfg.logPathToday)
if not os.path.exists(pathcfg.imagePathToday):
    os.makedirs(pathcfg.imagePathToday)
if not os.path.exists(pathcfg.reportPathToday):
    os.makedirs(pathcfg.reportPathToday)

# 用例存放路径
casePath = os.path.join(pathcfg.proPath, "testCase", "case")
# 用例列表路径
caseListFile = os.path.join(pathcfg.proPath, "caseList.txt")

def set_case_discover(rule='*_st.py'):
    '''
    生成测试用例集discover
    '''
    discover = unittest.defaultTestLoader.discover(casePath, pattern=rule, top_level_dir=None)
    return discover

@tomorrow.threads(4)
def runAll(testSuite):
    '''
    执行测试用例
    '''
    try:
        log.info('开始执行测试用例')
        result = BeautifulReport.BeautifulReport(testSuite)
        reportPathToday = pathcfg.reportPathToday
        reportFile = '测试报告' + pathcfg.nowTime
        result.report(filename=reportFile, description='自动化测试报告',log_path=reportPathToday)
    except Exception as e:
        log.error('用例执行失败，原因是：%s' % e)
        raise

if __name__ == '__main__':
    # 多线程执行，只生成一份报告
    discover = set_case_discover()
    for suite in discover:
        runAll(suite)
        #for case in suite:
        #    runAll(case)






