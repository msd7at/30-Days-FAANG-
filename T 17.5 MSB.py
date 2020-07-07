# link:https://www.geeksforgeeks.org/find-significant-set-bit-number/

# O(1)solution
def setBitNumber(n): 
  
    # Below steps set bits after 
    # MSB (including MSB) 
   
    # Suppose n is 273 (binary  
    # is 100010001). It does following 
    # 100010001 | 010001000 = 110011001 
    n |= n>>1
   
    # This makes sure 4 bits 
    # (From MSB and including MSB) 
    # are set. It does following 
    # 110011001 | 001100110 = 111111111 
    n |= n>>2   
   
    n |= n>>4  
    n |= n>>8
    n |= n>>16
       
    # Increment n by 1 so that 
    # there is only one set bit 
    # which is just before original 
    # MSB. n now becomes 1000000000 
    n = n + 1
   
    # Return original MSB after shifting. 
    # n now becomes 100000000 
    return (n >> 1) 
  
# Driver code 
  
n = 273            
print(setBitNumber(n)) 



# simple solution (brute force)
def setBitNumber(n): 
	if (n == 0): 
		return 0; 

	msb = 0; 
	while (n > 1): 
		n = int(n / 2); 
		msb += 1; 

	return (1 << msb); 

# Driver code 
n = 0; 
print(setBitNumber(n)); 
	
# This code is contributed 
# by mits 
