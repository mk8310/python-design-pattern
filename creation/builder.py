#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
@author     : ming
@file       : builder
@date       : 2017/10/15 23:10:01
@create by  : PyCharm Community Edition
@description:
    这段代码演示了建造者模式，该模式又称之为生成器模式。
"""

from abc import ABCMeta, abstractmethod


class Food(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print("%s is ready." % self.name)

    @property
    def name(self):
        pass

    def eat(self):
        print("Eat the %s" % self.name)


###########################################

class Hamburger(Food):
    @property
    def name(self):
        pass

    __metaclass__ = ABCMeta


class SpicyHamburger(Hamburger):
    @property
    def name(self):
        return "spicy hamburger."


class ChickenHamburger(Hamburger):
    @property
    def name(self):
        return "chicken hamburger"


class CodHamburger(Hamburger):
    @property
    def name(self):
        return "cod hamburger"


############################################

class ChickenDrumstick(Food):
    @property
    def name(self):
        pass

    __metaclass__ = ABCMeta


class SpicyChickenDrumstick(ChickenDrumstick):
    @property
    def name(self):
        return "spicy chicken drumstick"


class NewOrleansRoastedWing(ChickenDrumstick):
    @property
    def name(self):
        return "new orleans roasted wing"


##############################################

class Drink(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print("%s is ready." % self.name)

    @property
    def name(self):
        pass

    def drink(self):
        print("Drink the %s" % self.name)


class Cola(Drink):
    @property
    def name(self):
        return "cola"


class Juice(Drink):
    @property
    def name(self):
        return "juice"


#################################################

class FrenchFries(Food):
    @property
    def name(self):
        return "french fries"


#################################################

class SetMealBuilder(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._part_list = []

    @abstractmethod
    def build_hamburger(self):
        pass

    @abstractmethod
    def build_french_fries(self):
        pass

    @abstractmethod
    def build_chicken_drumstick(self):
        pass

    @abstractmethod
    def build_drink(self):
        pass

    @property
    def part_list(self):
        return self._part_list


class SetMeal1Builder(SetMealBuilder):
    def build_chicken_drumstick(self):
        self._part_list.append(SpicyChickenDrumstick())

    def build_drink(self):
        self._part_list.append(Cola())

    def build_french_fries(self):
        self._part_list.append(FrenchFries())

    def build_hamburger(self):
        self._part_list.append(SpicyHamburger())


class SetMeal2Builder(SetMealBuilder):
    def build_chicken_drumstick(self):
        self._part_list.append(NewOrleansRoastedWing())

    def build_drink(self):
        self._part_list.append(Juice())

    def build_french_fries(self):
        pass

    def build_hamburger(self):
        self._part_list.append(ChickenHamburger())


class SetMeal3Builder(SetMealBuilder):
    def build_chicken_drumstick(self):
        pass

    def build_drink(self):
        self._part_list.append(Juice())

    def build_french_fries(self):
        self._part_list.append(FrenchFries())

    def build_hamburger(self):
        self._part_list.append(CodHamburger())


class SetMealBuilderFactory(object):
    @staticmethod
    def CreateSetMealBuilder(set_meal_index):
        if set_meal_index == 1:
            return SetMeal1Builder()
        if set_meal_index == 2:
            return SetMeal2Builder()
        if set_meal_index == 3:
            return SetMeal3Builder()
        raise Exception("Your set meal not exists.")


##################################################

class WorkerDirector(object):
    __metaclass__ = ABCMeta

    def __init__(self, builder: SetMealBuilder):
        self._builder = builder

    @abstractmethod
    def build(self):
        pass


class Worker1(WorkerDirector):
    def build(self):
        self._builder.build_chicken_drumstick()
        self._builder.build_drink()
        self._builder.build_french_fries()
        self._builder.build_hamburger()
        return self._builder.part_list


class Worker2(WorkerDirector):
    def build(self):
        self._builder.build_french_fries()
        self._builder.build_hamburger()
        self._builder.build_chicken_drumstick()
        self._builder.build_drink()
        return self._builder.part_list


class WorkerFactory(object):
    @staticmethod
    def CreateWorker(worker_index, set_meal_builder):
        if worker_index == 1:
            return Worker1(set_meal_builder)
        if worker_index == 2:
            return Worker2(set_meal_builder)
        raise Exception("Your worker not exists.")


########################################################

def main():
    import sys
    set_meal_index = 1
    worker_index = 1
    if len(sys.argv) >= 2:
        set_meal_index = int(sys.argv[1])
    if len(sys.argv) >= 3:
        worker_index = int(sys.argv[2])

    set_meal_builder = SetMealBuilderFactory.CreateSetMealBuilder(set_meal_index)
    worker = WorkerFactory.CreateWorker(worker_index, set_meal_builder)
    results = worker.build()
    for result in results:
        if hasattr(result, 'eat'):
            result.eat()
        elif hasattr(result, 'drink'):
            result.drink()


if __name__ == '__main__':
    main()
