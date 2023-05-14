import unittest
from Intersection_of_two_arrays import intersection_of_two_arrays

class intersection_of_two_arrays_test(unittest.TestCase):

    def TestIntersection(self):
       assert intersection_of_two_arrays([1,2,3,4] , [2,3,4]) == [2,3,4]
       print("Did I manage to pass the test cases")


if __name__ == '__main__':
    unittest.main()
