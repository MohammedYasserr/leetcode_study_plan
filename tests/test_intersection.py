import unittest
import sys

# Importing the file containg the directory to the environment OS
sys.path.append('E:/Current/Projects/ds_workplace')
# print("sys.path.append('E:/Current/Projects/ds_workplace')")

from Intersection_of_two_arrays.intersection_of_two_arrays import intersection

class TestIntersection(unittest.TestCase):

    def test_intersection(self):
        """
        This Test case shows that there is intersection between the two input arrays
        """
        nums1 = [1,2,3,4]
        nums2 = [2,3]
        result = intersection(nums1,nums2)
        self.assertEqual(result, {2,3})
        print("Test Passed ! ")
    

    print("This is me from test file")