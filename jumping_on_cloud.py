def jumpingonclouds(c):
    jump = 0
    i = 0 
    n = len(c)
    while i < n-1:
        if ( i+2 < n and c[i+2] == 0 ):
            jump += 1 
            i = i+2
            
        elif ( i+1 < n and c[i+1] == 0):
            jump += 1 
            i = i+1 
    return jump         
 
    
    
c = [0,0,0,0,0,1,0]
#c = [0,1,0,0,0,1,0]
#c = [0,0,1,0,0,1,0]
result = jumpingonclouds(c)
print(result)
