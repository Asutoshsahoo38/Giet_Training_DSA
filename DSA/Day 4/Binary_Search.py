#Binary search
def Binary_search(array,x,low,high):
    while low <= high:
        mid = (low + high)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return -1
array = [3,4,5,6,7,8,9]
x = 9
result = Binary_search(array,x,0,len(array)-1)
if result != -1:
    print("Element found at index :",str(result))
else:
    print("Not found")