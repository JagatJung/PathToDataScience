# Begin with the mid element of the whole array as search key.
# If the value of the search key is equal to the item then return index of the search key.
# Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise, narrow it to the upper half.
# Repeatedly check from the second point until the value is found or the interval is empty.

from array import array


def getMiddleElement(x):

    if x%2==0:
        return int(x/2)

    else:
        return int(x/2+1)


def theSearcher(tofind, searchList):
    
    midnum= getMiddleElement(len(searchList))
    print(searchList)
    print (midnum)
    if(midnum>1):

        if(tofind == searchList[midnum]):
            print("match Found")

        elif tofind < searchList[midnum]:
            searchList = searchList[:midnum]
            theSearcher(tofind, searchList)
        
        elif tofind > searchList[midnum]:
            searchList = searchList[midnum:]
            theSearcher(tofind, searchList)
        
    else: 
        print("Match not found")


tofind=8

searchList=[121,22,30,54,1,29,8]

# sorting the list
searchList.sort()

theSearcher(tofind,searchList)








