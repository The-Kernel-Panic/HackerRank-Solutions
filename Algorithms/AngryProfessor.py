#Practice > Algorithms > Implementation > AngryProfessor

def aP(k,a): #Will class be cancelled?
    s = 0 #number of ontime students.
    for i in a:
        if i <= 0:
            s += 1
    if s >= k:
        ans = "NO"
    else:
        ans = "YES"
    return ans

'''
For testing:
k = 2 #minimum early students required.
a = [0, -1, 2, 1]
print(aP(k,a))
'''
