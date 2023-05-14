import unittest
import intersection_of_two_arrays 

class intersection_of_two_arrays_test(unittest.TestCase):

    def test_intersection_of_two_arrays(self):
       assert intersection_of_two_arrays([1,2,3,4] , [2,3,4]) == [2,3,4]
       print("Did I manage to pass the test cases")

