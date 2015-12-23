import skilstak.colors as c
import math
import time
def solve_acceleration():
    v = int(input(c.cl + "What is the initial velocity of the object? >>> "))
    f = int(input(c.cl + "What is the final velocity of the object? >>> "))
    t = int(input(c.cl + "What is the time between the initial and final velocities? >>> "))
    v1 = float(v)
    v2 = float(f)
    t1 = float(t)
    a = v2 - v1/t
    print(c.cl + "The acceleration of the object is " + str(a) + " m/s^2.")

def solve_kinetic():
    m = int(input(c.cl + "What is the mass of your object? >>> "))
    v = int(input(c.cl + "What is the velocity, in m/s, of your object? >>> "))
    m1 = float(m)
    v1 = float(v)
    k = m1 * v1**2
    k1 = k/2
    print(c.cl + "The kinetic energy of the object is " + str(k1) + " joules.")
