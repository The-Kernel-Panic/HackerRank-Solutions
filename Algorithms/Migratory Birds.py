#HackerRank Practice > Algorithms > Implementation > Migratory Birds

import collections



def migratoryBirds(arr):
    dict1 = dict(collections.Counter(arr))
    values = [i for i in dict1.values()]
    max_value = max(values)
    l1 = [key for key, value in dict1.items() if value == max_value]
    ans = min(l1)
    return ans

'''
For testing:
arr = [5, 4, 4, 4, 5, 5, 2] #Can be any array.
print(migratoryBirds(arr))
'''
