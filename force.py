import skilstak.colors as c
import math

def force():
    print(c.cl + "What is the mass of the object in meters?")
    m = input(">>> ")
    print(c.cl + "What is the acceleration of the object, in m/s^2?")
    a = input(">>> ")
    m = int()
    a = int()
    f = a * m
    print(c.cl + "The force acting on the object is ",f + "joules.")
