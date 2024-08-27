
def palidrome_number(x: int) -> bool: 
    
    s = str(x)    
    print(s)
    print(type(s))
    
    # if x < 10:
    #     print("This number is samller than 10")
    #     return True
    
    # handle the edge case where the string begins with a minus sign(it is not a palindrome)
    if s.startswith("-") :
        print("False")
        return False
    
    if len(s) == 1:
        print("True")
        return True
    
    # perform the two pointers technique afterwards 
    i=0
    j=len(s)-1
    # as long as the i is at index samller than the j
    while i < j :
        if s[i] == s[j]:
            i += 1 
            j += 1
        else:
            # print(False)
            return False
    return True
            

palidrome_number(1000021)
