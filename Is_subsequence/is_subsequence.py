# Solving is subsequence - leetcode 


# def isSubsequence(s:str,t:str) -> bool :
     
        
#     """
#     Checking whether the string s is a subsequence of string t
#     """
        
#     if len(s) > len(t):
#         return False

#     # Loop over the s sting
#     for i in range(0,len(s)):
        
#         try:
#             index = t.index(s[i])
#         except ValueError:
#             return False
#             # Update the t string 
#         t = t[index+1:]
            
#         return True
    

# print(isSubsequence("abc","fxacb")) #True
# print(isSubsequence("abc","afcb"))
# print(isSubsequence("rt" , "xbc")) #False
# # print(isSubsequence("","etjh"))

            
def isSubsequence(s:str,t:str):
    
    """
    Checking whether the string s is a subsequence of string t
    """
    remainder_of_t = iter(t)
    
    for char in s : 
        if char not in remainder_of_t:
            return False
    return True

print(isSubsequence("abc","fxabc")) # True
print(isSubsequence("abc","afcb")) # False - Relative order condition fails.
print(isSubsequence("","")) # True - Empty String is a substring of an empty string.
print(isSubsequence("" , "lty")) # True - Empty string is a substring of any string.
