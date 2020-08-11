#HackerRank Practice > Algorithms > Warmup > TimeConversion

def time(s):
    if s[-2:] == "AM":
        if s[:2] != "12":
            new_time = s[:-2]
        elif s[:2] == "12":
            new_time = s.replace("12", "00", 1)
            new_time = new_time[:-2]
    elif s[-2:] == "PM":
        if s[:2] != "12":
            s2 = int(s[:2]) + 12
            new_time = str(s2) + s[2:]
            new_time = new_time[:-2]
        elif s[:2] == "12":
            new_time = s[:-2]
    else:
        new_time = "Invalid Number"
    return new_time

#This part is optional

#Python program to convert time from 12hr format to 24hr

#time[-2:] -> am or pm
#time[:-2] -> time without am or pm
#time[2:] -> time without the first 2 digits
#time[:2] -> the first 2 digits

old_time = input("Enter the time 12hr format [hh:mm:ssAM/PM]")
print("The time in 24hr format is: " + time(old_time))
