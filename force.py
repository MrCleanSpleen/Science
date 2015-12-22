import skilstak.colors as c
import math

def force():
    """Uses Newton's second law to find the force acting on an object.

    F = m x a
    """
    print(c.cl + "What is the mass of the object in kilograms?")
    m = int(input(">>> "))
    print(c.cl + "What is the acceleration of the object, in m/s^2?")
    a = int(input(">>> "))
    m1 = float(m)
    a1 = float(a)
    f = float(a1 * m1)
    print(c.cl + "The force acting on the object is " + str(f) + " joules.")
