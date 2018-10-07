### binary search
### O(log n)

def binarySearch(x, intList):
    # returns True if x is in intList, False otherwise, 
    # x is an integer, intList is a sorted list of integers
    if len(intList)==1:
        # base case
        if intList[0]==x:
            return True
        else:
            return False
    else:
        n1 = len(intList) // 2
        # inductive step
        if x<intList[n1-1]:
            return binarySearch(x, intList[:n1])
        if x>intList[n1-1]:
            return binarySearch(x, intList[n1:])
        if x==intList[n1-1]:
            return True


intList = [ 3, 10, 11, 15, 23, 25, 38, 45, 49, 69, 81]
xList=[45, 13, 4, 60, 23]
out=[]
for x in xList:
    out.append([x, binarySearch(x, intList)])
print(out)
# This should show
# [[45, True], [13, False], [4, False], [60, False], [23, True]]
