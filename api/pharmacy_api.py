#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import hashlib
import time
import requests

AppKey = "6a9c4160fb813859190f8d307990a4f1"
AppSecret="e8dd6aae2043"
CurTime = str(int((time.time() * 1000)))
Nonce = hashlib.new('sha512',str(time.time()).encode("utf-8")).hexdigest()
CheckSum = hashlib.sha1((AppSecret + CurTime + Nonce).encode("utf-8")).hexdigest()

class TestLogin:
    def ecn_login(self, CurTime=CurTime, AppKey=AppKey, CheckSum=CheckSum, Nonce=Nonce):
        url = "http://192.168.1.208:9191/pharmacy/user/login"
        """
            AppKey	开发者平台分配的appkey
            Nonce	随机数（最大长度128个字符）
            CurTime	当前UTC时间戳，从1970年1月1日0点0 分0 秒开始到现在的秒数(String)
            CheckSum	SHA1(AppSecret + Nonce + CurTime)，三个参数拼接的字符串，进行SHA1哈希计算，转化成16进制字符(String，小写)
        """
        header = {
                "Content-Type" : "application/x-www-form-urlencoded;charset=utf-8",
                "AppKey" : AppKey,
                "CurTime" : CurTime,
                "CheckSum" : CheckSum,
                "Nonce" : Nonce
        }
        data = {
                "loginName" : "15829087848",
                "password" : "4a7d1ed414474e4033ac29ccb8653d9b"
        }
        res = requests.request(method="GET", url = url, headers = header, params= data)
        result = res.status_code
        return result

    def getOderList(self, CurTime=CurTime, AppKey=AppKey, CheckSum=CheckSum, Nonce=Nonce):
        url = "http://192.168.1.208:9191/pharmacy/order/supOrderList"
        """
           AppKey	开发者平台分配的appkey
           Nonce	随机数（最大长度128个字符）
           CurTime	当前UTC时间戳，从1970年1月1日0点0 分0 秒开始到现在的秒数(String)
           CheckSum	SHA1(AppSecret + Nonce + CurTime)，三个参数拼接的字符串，进行SHA1哈希计算，转化成16进制字符(String，小写)
        """
        header = {
            "Content-Type": "application/json;charset=utf-8",
            "AppKey": AppKey,
            "CurTime": CurTime,
            "CheckSum": CheckSum,
            "Nonce": Nonce
        }
        data = {
            "distributionType" : None,
            "endTime" : "20220418",
            "headSupplierId" : "3af807e8d44046e1a55a64eb66d63349",
            "pageIndex" : 1,
            "pageSize" : 10,
            "roleList" : ["ac1472328a944fd992d742e11cb598ee"],
            "startTime" : "20220319"
        }
        #获取订单列表
        result = requests.request(method="POST", url=url, headers=header, data=data)
        return result

    def geConsultData_New(self,  CurTime=CurTime, AppKey=AppKey, CheckSum=CheckSum, Nonce=Nonce):
        url = "http://192.168.1.208:9191/pharmacy/consult/getConsultListByParam"
        """
                   AppKey	开发者平台分配的appkey
                   Nonce	随机数（最大长度128个字符）
                   CurTime	当前UTC时间戳，从1970年1月1日0点0 分0 秒开始到现在的秒数(String)
                   CheckSum	SHA1(AppSecret + Nonce + CurTime)，三个参数拼接的字符串，进行SHA1哈希计算，转化成16进制字符(String，小写)
        """
        header = {
            "Content-Type": "application/json;charset=utf-8",
            "AppKey" : AppKey,
            "CurTime" : CurTime,
            "CheckSum" : CheckSum,
            "Nonce" : Nonce
        }
        data = {
            "lookupId" : "phar_10000004203",
            "pageIndex" : 1,
            "pageSize" : 10,
            "pharmacyId" : "83360dda77ff444a89f7a45beadc8f87",
            "status" : "2",
            "signId" : None
        }
        result = requests.request(method="POST", url=url, headers=header, data=data)
        return result