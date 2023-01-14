#the program outputs the max number of each sub array
#here the function takes array, array size, sub array size as a argument
def max_subarray(arr,n,k):
    
    for i in range(n-k):
        max = arr[i]
        for j in range(k):
            if (max < arr[i+j]):
                max = arr[i+j]
    print(max)                
                
              

       

arr = [10,70,12,13,15,23,100,60,5]
n = 9
k=3
print("Max of sub array is: ",max_subarray(arr,n,k))
