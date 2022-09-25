orbits = [(1,3), (2.5,10), (7,2), (6,6), (4,3)]

def find_farthest_orbit(orbit):
    a = (0,0)
    for i in orbit:
        if i[-1] > a[-1]:
            a = i
    print(a)

find_farthest_orbit(orbits)

