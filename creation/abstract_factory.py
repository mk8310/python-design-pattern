#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
@author     : ming
@file       : abstract_factory
@date       : 2017/10/15 22:25:19
@create by  : PyCharm Community Edition
@description:
    这段代码演示了抽象工厂模式，该模式又称为Kit模式，该模式解决了拥有多个产品族情况下对象创建的业务抽象问题。
    使用者只需要知道自己需要使用的产品族即可，而无需知道具体该产品族下属有多少个具体的产品类
"""

import sys
from abc import ABCMeta, abstractmethod


class Account(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_catalog(self):
        pass
        # print("I'm %s." % self._account_name)


class Register(Account):
    def show_catalog(self):
        print("This is a registered account.")


class Anonymous(Account):
    def show_catalog(self):
        print("This is an anonymous user.")


#############################################

class Role(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_role(self):
        pass


class Administrator(Role):
    def show_role(self):
        print("I'm a administrator.")


class Operator(Role):
    def show_role(self):
        print("I'm an operator.")


class Seller(Role):
    def show_role(self):
        print("I'm a seller.")


class Purchaser(Role):
    def show_role(self):
        print("I'm a purchaser.")


#############################################

class AccountFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def create_role(self):
        pass


class AdministratorFactory(AccountFactory):
    def create_account(self):
        return Register()

    def create_role(self):
        return Administrator()


class OperatorFactory(AccountFactory):
    def create_account(self):
        return Register()

    def create_role(self):
        return Operator()


class RegisteredSellerFactory(AccountFactory):
    def create_role(self):
        return Seller()

    def create_account(self):
        return Register()


class AnonymousSellerFactory(AccountFactory):
    def create_role(self):
        return Seller()

    def create_account(self):
        return Anonymous()


class RegisteredPurchaserFactory(AccountFactory):
    def create_role(self):
        return Purchaser()

    def create_account(self):
        return Register()


class AnonymousPurchaserFactory(AccountFactory):
    def create_role(self):
        return Purchaser()

    def create_account(self):
        return Anonymous()


def main():
    role_type = ""
    account_type = ""
    if len(sys.argv) >= 2:
        role_type = sys.argv[1]
    if len(sys.argv) >= 3:
        account_type = sys.argv[2]
    if role_type == "admin":
        factory = AdministratorFactory()
    elif role_type == "opr":
        factory = OperatorFactory()
    elif role_type == "seller" and account_type == "reg":
        factory = RegisteredSellerFactory()
    elif role_type == "purchaser" and account_type == "reg":
        factory = RegisteredPurchaserFactory()
    elif role_type == "seller" and account_type != "reg":
        factory = AnonymousSellerFactory()
    else:
        factory = AnonymousPurchaserFactory()
    account = factory.create_account()
    role = factory.create_role()
    account.show_catalog()
    role.show_role()


if __name__ == "__main__":
    main()
