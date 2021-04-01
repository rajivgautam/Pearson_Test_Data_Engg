"""
Question 3.
Imagine a never ending number is created by concatenating numbers to it in order. 
The number starts 123456789101112...  You can see the 11th digit is 0 and the 
15th digit will be 2. 

Write a function that can compute the nth digit of this never ending number.
(Bonus if you can compute the nth digit without using a String) 
"""

def getNthDigit(n):  
    
    s = ""        
    c = 1    
  
    # add integers in string
    while(True) :          
        if (c < 10):
            s += chr(48 + c)  
        
        else:
            s1 = ""
            dup = c
  
            # add the number in string
            while (dup > 0):
                s1 += chr((dup % 10) + 48)
                dup //= 10
  
            # reverse the string
            s1 = "".join(reversed(s1)) 
  
            # attach the number
            s += s1
        c += 1
  
        # if the length exceeds N
        if (len(s) >= n):
            return int(s[n - 1])

print(getNthDigit(15))