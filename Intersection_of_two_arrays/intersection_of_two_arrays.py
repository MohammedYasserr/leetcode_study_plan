from typing import List


def intersection(nums1: List[int] , nums2: List[int]) -> List[int]:
    # Checking the Edge cases when one of the two input arrays are empty
    return set(nums1) & set(nums2)


print(intersection([1, 2, 3, 4], [2, 3])) 

"""
complexity analysis of using AND Bitwise 
"""
