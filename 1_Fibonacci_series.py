"""
Question 1
Write a function printFib(n) that prints the Fibonacci series until
a value would exceed the input n.
For example  printFib(30) would print the numbers
0, 1, 1, 2, 3, 5, 8, 13, 21

Remember : The Fibonacci Sequence is the series of numbers
where the first two numbers in the sequence are 0, 1, then after 
that to calculate the next number sum the previous two numbers in the
sequence. 
"""
def printFib(n):
    
    nterms = n
    lst =[]      
    
    #### inner function
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))
                
    
    #### check if the number n valid
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:        
        for i in range(nterms):
            rec_val = recur_fibo(i)            
            lst.append(rec_val)            
            if nterms < lst[i]:
                lst.pop()
                break
         
    return lst

print(printFib(30))