#HackerRank Practice > Algorithms > Implementation > Beautiful Days at the Movies

'''
Given a range of numbered days between i and j, and a number k , determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers where |x - reverse(x)| is evenly divisible by k .
If a day's value is a beautiful number, it is a beautiful day.
Print the number of beautiful days in the range.
'''

def beautifulDays(i,j,k):
    count = 0
    for x in range(i, j+1):
        if (x - int(str(x)[::-1])) % k == 0:
            count += 1
    return(count)
