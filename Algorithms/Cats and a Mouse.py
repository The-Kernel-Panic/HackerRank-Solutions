#HackerRank Practice > Algorithms > Implementation > Cats and a Mouse


def catAndMouse(x,y,z):
    d_c1 = z - x
    d_c2 = z - y

    if d_c1 < 0:
        d_c1 = d_c1 * -1
    if d_c2 < 0:
        d_c2 = d_c2 * -1

    if d_c1 > d_c2:
        ans = "Cat B"
    elif d_c2 > d_c1:
        ans = "Cat A"
    elif d_c1 == d_c2:
        ans = "Mouse C"
    return ans

'''
For testing:
x = 1 #Cat A
y = 3 #Cat B
z = 2 #Mouse C
print(catAndMouse(x,y,z))
'''
