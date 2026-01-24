import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(cummulative_sum(test_list), 45)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(cummulative_sum(test_list), 0)

    def test_single_list(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(cummulative_sum(test_list), 6)

    def test_single_number(self):
        test_list = [[1]]
        self.assertEqual(cummulative_sum(test_list), 1)

    def test_negative_numbers(self):
        test_list = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(cummulative_sum(test_list), -45)

    def test_mixed_numbers(self):
        test_list = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]
        self.assertEqual(cummulative_sum(test_list), 0)

    def test_invalid_input(self):
        test_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            cummulative_sum(test_list)
