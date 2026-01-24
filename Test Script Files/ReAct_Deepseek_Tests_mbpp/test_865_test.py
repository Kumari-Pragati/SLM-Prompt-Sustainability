import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5]
        n = 3
        expected_result = [3, 6, 9, 12, 15]
        self.assertEqual(ntimes_list(nums, n), expected_result)

    def test_edge_case_zero(self):
        nums = [1, 2, 3, 4, 5]
        n = 0
        expected_result = [0, 0, 0, 0, 0]
        self.assertEqual(ntimes_list(nums, n), expected_result)

    def test_edge_case_negative(self):
        nums = [1, 2, 3, 4, 5]
        n = -1
        expected_result = [-1, -2, -3, -4, -5]
        self.assertEqual(ntimes_list(nums, n), expected_result)

    def test_empty_list(self):
        nums = []
        n = 3
        expected_result = []
        self.assertEqual(ntimes_list(nums, n), expected_result)

    def test_single_element(self):
        nums = [5]
        n = 2
        expected_result = [10]
        self.assertEqual(ntimes_list(nums, n), expected_result)
