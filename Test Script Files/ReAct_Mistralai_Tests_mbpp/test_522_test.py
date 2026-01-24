import unittest
from mbpp_522_code import lbs

class TestLbsFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(lbs([]), 0)

    def test_single_element_list(self):
        for num in range(1, 6):
            self.assertEqual(lbs([num]), 1)

    def test_increasing_list(self):
        test_list = [1, 2, 3, 4, 5]
        expected_result = len(test_list) - 1
        self.assertEqual(lbs(test_list), expected_result)

    def test_decreasing_list(self):
        test_list = [5, 4, 3, 2, 1]
        expected_result = len(test_list) - 1
        self.assertEqual(lbs(test_list), expected_result)

    def test_mixed_list(self):
        test_list = [1, 5, 2, 4, 3]
        expected_result = 4
        self.assertEqual(lbs(test_list), expected_result)

    def test_duplicate_elements(self):
        test_list = [1, 1, 2, 3, 4]
        expected_result = 4
        self.assertEqual(lbs(test_list), expected_result)

    def test_negative_numbers(self):
        test_list = [-1, -2, -3, -4, -5]
        expected_result = 9
        self.assertEqual(lbs(test_list), expected_result)

    def test_zero(self):
        self.assertEqual(lbs([0]), 1)
