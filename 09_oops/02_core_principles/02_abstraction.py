#Topic: Abstraction in Python

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):

    def start_engine(self):
        print("Car engine started with key ignition")


class Bike(Vehicle):

    def start_engine(self):
        print("Bike engine started with self start")


# Creating objects
c1 = Car()
b1 = Bike()

c1.start_engine()
b1.start_engine()