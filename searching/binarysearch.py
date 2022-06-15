# Begin with the mid element of the whole array as search key.
# If the value of the search key is equal to the item then return index of the search key.
# Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise, narrow it to the upper half.
# Repeatedly check from the second point until the value is found or the interval is empty.

import math


def getMiddleElement(low, high):
    midnum= low + (high-low)/2
    return int(math.ceil(midnum))


def theSearcher(low, high, tofind, searchList):
    
    midnum= getMiddleElement(low, high)
    print(searchList)
    print (midnum)
    if(midnum>0):

        if(tofind == searchList[midnum]):
            print("match Found")

        elif tofind < searchList[midnum]:
            searchList = searchList[:midnum]
            theSearcher(0,len(searchList)-1,tofind, searchList)

        elif tofind > searchList[midnum]:
            searchList = searchList[midnum:]
            theSearcher(0,len(searchList)-1,tofind, searchList)
    else: 
        print("Match not found")


tofind=int(input("Enter the number to find"))

searchList=[121,22,30,54,1,29,8]

# sorting the list
searchList.sort()

theSearcher(0, len(searchList)-1,tofind,searchList)








