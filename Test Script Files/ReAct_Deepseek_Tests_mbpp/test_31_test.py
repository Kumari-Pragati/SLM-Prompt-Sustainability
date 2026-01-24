import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 2
        expected_output = [3, 4]
        self.assertEqual(func(nums, k), expected_output)

    def test_edge_case_k_equals_zero(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 0
        expected_output = []
        self.assertEqual(func(nums, k), expected_output)

    def test_edge_case_k_greater_than_number_of_unique_elements(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 10
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(func(nums, k), expected_output)

    def test_edge_case_empty_list(self):
        nums = []
        k = 2
        expected_output = []
        self.assertEqual(func(nums, k), expected_output)

    def test_edge_case_single_element(self):
        nums = [[1]]
        k = 1
        expected_output = [1]
        self.assertEqual(func(nums, k), expected_output)

    def test_edge_case_k_equals_to_number_of_unique_elements(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 5
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(func(nums, k), expected_output)
