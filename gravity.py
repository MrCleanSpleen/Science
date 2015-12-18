import math
import skilstak.colors as c

def solve_universalgravity():
    print(c.cl + c.base03 + "What is the mass of the first object? (In Kilograms)")
    m1 = input(">>> ")
    print(c.cl + "What is the mass of the second object? (In Kilograms)")
    m2 = input(">>> ")
    print(c.cl + "What is the distance between the two objects? (In Meters)")
    d = input(">>> ")
    d = float()
    m1 = float()
    m2 = float()
    pm = float(2.17651 * 10**-8)
    pl = float(1.616199 * 10**-35)
    pt = float(539106 * 10**-44)
    G = float(pl**3/pm * pt**2)
    m3 = float(m1 * m2)
    d2 = float(d * d)
    F1 = G * m3
    F2 = F1/d2
    print(c.cl + "The amount of force between the two objects is, in joules, ",F2) 
