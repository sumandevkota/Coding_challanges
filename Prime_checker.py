print("Please Enter positive number only!!")
x = int(input("Enter a number to check prime: "))
flag = False

if x > 1:
    for i in range(2,x):
        if ((x % i) == 0):
            flag = True
            break
else:
    print("Dont enter zero or Negative numbers!!!!")        
       
if flag == True:
    print(x, "is NOT PRIME!!")
else:
    print(x,"is PRIME!!!")            

 