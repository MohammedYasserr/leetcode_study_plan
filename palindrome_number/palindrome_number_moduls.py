
def palindrome_numer(x:int) -> bool:
    '''
    Solving the valid palindrome number using moduls approach
    '''
    
    if x == 0:
        return True
    
    if x < 0 or x % 10 == 0:
        return False
    
    original = x
    print(f"This value doesn't change {original}")
    revresed_number = 0 
    
    while x > 0:
        
        #extract the last digit 
        last_digit = x % 10
        print(f"This is the last digit:{last_digit}")
        
        # Append the digit to the revresed number
        revresed_number = revresed_number * 10 + last_digit
        print(f"This is the reversed number:{revresed_number}")
        
        x = x // 10 
        print(f"This is the updated value of x after floor division:{x}")
    
    # check if the reversed number is the same as the original one
    print(revresed_number == original)
    return revresed_number == original


palindrome_numer(101)