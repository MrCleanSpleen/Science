import math
import skilstak.colors as c

def solve_universalgravity():
    print(c.cl + c.base03 + "What is the mass of the first object? (In Kilograms)")
    m1 = input(">>> ")
    print(c.cl + "What is the mass of the second object? (In Kilograms)")
    m2 = input(">>> ")
    print(c.cl + "What is the distance between the two objects? (In Meters)")
    d = input(">>> ")
    d = int()
    m1 = int()
    m2 = int()
    pm = int(2.17651 * 10**-8)
    pl = int(1.616199 * 10**-35)
    pt = int(539106 * 10**-44)
    G = int(pl**3/pm * pt**2)
    m3 = int(m1 * m2)
    d2 = int(d * d)
    F = G * m3/d2
    print(c.cl + "The amount of force between the two objects is, in joules, ",F) 
