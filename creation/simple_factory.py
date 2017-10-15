#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
@author     : ming
@file       : simple_factory
@date       : 2017/10/15 21:59:56
@create by  : PyCharm Community Edition
@description:
    该段代码演示了简单工厂模式，该模式可以有效的解耦类的实现（产品）与创建（工厂）之间的关系。
    该模式最大的缺点为每次新增产品都需要在工厂类新增具体的实现，不符合开闭原则
"""

import sys

from abc import ABCMeta, abstractmethod


class Account(object):
    """ 产品基类 """
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def _show_role(self):
        pass

    def show_detail(self):
        print("I'm %s." % self._name)
        self._show_role()


class Administrator(Account):
    """ 具体产品类1 """

    def _show_role(self):
        print("I'm a administrator.")


class Operator(Account):
    """ 具体产品类2 """

    def _show_role(self):
        print("I'm an operator.")


class Register(Account):
    """ 具体产品类3 """

    def _show_role(self):
        print("I'm a register.")


class Anonymous(Account):
    """ 具体产品类4 """

    def _show_role(self):
        print("I'm an anonymous user.")


##############################################

class AccountFactory(object):
    """ 工厂类 """

    def create_account(self, account_description, account_name):
        if account_description == "admin":
            return Administrator(account_name)
        elif account_description == "opr":
            return Operator(account_name)
        elif account_description == "user":
            return Register(account_name)
        else:
            return Anonymous(account_name)


##############################################

def main():
    account_description = ""
    account_name = ""
    if len(sys.argv) >= 3:
        account_description = sys.argv[1]
        account_name = sys.argv[2]
    if len(sys.argv) == 2:
        account_name = sys.argv[1]
    account_factory = AccountFactory()
    account = account_factory.create_account(account_description, account_name)
    account.show_detail()


if __name__ == "__main__":
    main()
