#!/usr/bin/Python
# -*- coding: utf-8 -*-
#执行者接口
class Executor(object):
    def run(self):
        pass
#数据解析模块执行者
class DataParserExecutor(Executor):
    def __init__(self,Handler,MongoClient,MySQLDB):
        self.Hander = Handler
        self.MongoClient = MongoClient
        self.MySQLDB = MySQLDB
#解析器
class Parser(object):
    def __init__(self,url,html):
        self.url = url
        self.html = html
    def parse(self,url,html):

        return Data
#公司页面解析器
class CompanyParser(Parser):
    def __init__(self,url,html):
        Parser.__init__(self,url,html)

    return CompanyData
#职位解析器
class JobParser(Parser):
    def __init__(self,url,html):
        Parser.__init__(self,url,html)

    return JobData

#数据接口
class Data(object):
    pass

#公司数据
class CompanyData(Data):
    pass
#职位数据
class JobData(Data):
    pass

#来源网站
class Website(object):
    def __init__(self,data):
        self.data = data
    def save(self,data):
        pass




