#Linear Search
def Linear_search(array,n,x):
    for i in  range(0,n):
        if(array[i] == x):
            return i
    return -1
array = [2,4,0,1,9]
x = 9
n = len(array)
result = Linear_search(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ",result)