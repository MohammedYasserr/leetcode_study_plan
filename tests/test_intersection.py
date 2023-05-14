import unittest
from Intersection_of_two_arrays import intersection_of_two_arrays

class intersection_of_two_arrays_test(unittest.TestCase):

    def TestIntersection(self):
        nums1 = [1,2,3,4]
        nums2 = [2,3]
        result = intersection_of_two_arrays(nums1,nums2)
        self.assertEqual(result, [2,3])
        print("Test Passed ! ")


if __name__ == '__main__':
    unittest.main()
