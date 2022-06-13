# <!-- Linear Search ( Array A, Value x)
# Step 1: Set i to 1
# Step 2: if i > n then go to step 7
# Step 3: if A[i] = x then go to step 6
# Step 4: Set i to i + 1
# Step 5: Go to Step 2
# Step 6: Print Element x Found at index i and go to step 8
# Step 7: Print element not found
# Step 8: Exit -->

needSearch = str(input("Enter the number"))

theList=["A","B","C","D","E"]

foundFlag = 0

print (needSearch)

for i in theList:
    if i is needSearch:
        foundFlag+=1
     

if foundFlag != 0:
    print("Match Found")
else:
    print("Match not found")
    



