def linearSearch(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            print(f"Given element is in {i} index")
            return i
    return -1

arr = [2,4,6,8,10,1,3,5,7,9]
n = int(input(("Enter element to search : ")))
a = linearSearch(arr,n)
if a == -1:
    print("Not presented ... ")
