"""
Fibonacci numbers:

    in mathmatics Fibonacci number is the sum of the two preceding fibonacci numbers.
    e.g F(3) = F(2) + F(1) = 2, note that the F(0) is omitted, and Fibonacci numbers start from F(1) where its equals to 1.
    
    To solve Fibonacci numbers problem we can use recursion algorithm to get the 2 previus numbers recursively.
"""

def get_fibonacci(position):
    
    if position <= 1:
        return position
    elif position >= 2:
      
        return get_fibonacci(position-1) + get_fibonacci(position-2)
   
        

# Test cases
print(get_fibonacci(9))
print(get_fibonacci(11))
print(get_fibonacci(0))