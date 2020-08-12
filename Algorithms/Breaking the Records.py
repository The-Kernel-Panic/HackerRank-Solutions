#Practice > Algorithms > Implementation > Breaking the Records

def record(scores):
    min = max = scores[0]
    count_max = count_min = 0
    #To find max
    for i in scores:
        if i > max:
            max = i
            count_max += 1
    #To find min
    for i in scores:
        if i < min:
            min = i
            count_min += 1
    result = count_max, count_min
    return result

'''
For testing:
print(record(scores2))
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
scores2 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
'''
