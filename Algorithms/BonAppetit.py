#HackerRank Practice > Algorithms > Implementation > Bon Appétit

def bonAppetit(bill,k,b):
    bill.pop(k)
    a_bill = int(sum(bill) / 2)
    if a_bill == b:
        print("Bon Appetit")
    else:
        print(b - a_bill)

'''
For testing:
bill = [3,10,2,9] #Total bill
k = 1 # index of fodd Ana didnt eat
b = 7 # Amount Brian charged her

bonAppetit(bill,k,b)
'''
