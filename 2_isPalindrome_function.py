"""
Question 2. 
Complete the function isPalindrome below so that  it returns 
True if the given string is a palindrome.  A palindrome is a string that is 
the same forwards and backwards. For example "bob", "9119", and "racecar" are
palindromes but "bar" and "palindrome" are not.
"""
def isPalindrome( s ):
    if s == s[::-1]:
        return True
    else:
        return False

print(isPalindrome("bob"))