#two sums leetcode problem with O(n^2) time 
def twoSum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if(arr[i] + arr[j] == target):
                if (i == j):
                    print("Same index added twice to achive target")
                else:
                    print("The index are ",i," & ",j)    
           
arr = [1,4,3,5,7]  
target = 7
twoSum(arr,target)          