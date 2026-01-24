import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_ntimes_list(self):
        self.assertEqual(ntimes_list([1,2,3], 2), [2,4,6])
        self.assertEqual(ntimes_list([-1,-2,-3], 2), [-2,-4,-6])
        self.assertEqual(ntimes_list([1,2,3,4,5], 3), [3,6,9,12,15])
        self.assertEqual(ntimes_list([-1,-2,-3,-4,-5], 3), [-3,-6,-9,-12,-15])
        self.assertEqual(ntimes_list([1,2,3,4,5,6], 0), [0,0,0,0,0,0])
        self.assertEqual(ntimes_list([-1,-2,-3,-4,-5,-6], 0), [0,0,0,0,0,0])

    def test_ntimes_list_empty_list(self):
        self.assertEqual(ntimes_list([], 2), [])

    def test_ntimes_list_single_element(self):
        self.assertEqual(ntimes_list([1], 2), [2])

    def test_ntimes_list_negative_numbers(self):
        self.assertEqual(ntimes_list([-1,-2,-3], -2), [2,-4,6])

    def test_ntimes_list_zero(self):
        self.assertEqual(ntimes_list([1,2,3], 0), [])
