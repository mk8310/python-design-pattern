#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
@author     : ming
@file       : factory_method
@date       : 2017/10/15 22:19:59
@create by  : PyCharm Community Edition
@description:
    该段代码演示了工厂方法模式,该模式在简单工厂模式的基础上解耦了具体的工厂类，使得在新增产品的情况下无需修改其他的工厂类而达到扩展系统的目的。
    该模式最大的缺点：在新增产品的情况下需要新增两套实现代码，容易增加系统复杂度。
    当系统只有一个产品的情况下，工厂方法模式退化为简单工厂模式。
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
    """ 工厂基类 """
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_account(self, account_name):
        pass


class AdministratorFactory(AccountFactory):
    """ 具体工厂类1 """

    def create_account(self, account_name):
        return Administrator(account_name)


class OperatorFactory(AccountFactory):
    """ 具体工厂类2 """

    def create_account(self, account_name):
        return Operator(account_name)


class RegisterFactory(AccountFactory):
    """ 具体工厂类3 """

    def create_account(self, account_name):
        return Register(account_name)


class AnonymousFactory(AccountFactory):
    """ 具体工厂类4 """

    def create_account(self, account_name):
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
    if account_description == "admin":
        account_factory = AdministratorFactory()
    elif account_description == "opr":
        account_factory = OperatorFactory()
    elif account_description == "user":
        account_factory = RegisterFactory()
    else:
        account_factory = AnonymousFactory()
    account = account_factory.create_account(account_name)
    account.show_detail()


if __name__ == "__main__":
    main()
