import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_single_element(self):
        self.assertEqual(find_Sum([10], 1), 10)

    def test_duplicate_elements(self):
        self.assertEqual(find_Sum([2, 2, 2, 2], 4), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Sum([-1, -2, -3, -4, -5], 5), -15)

    def test_mixed_numbers(self):
        self.assertEqual(find_Sum([-1, 2, -3, 4, -5], 5), 5)

    def test_large_numbers(self):
        self.assertEqual(find_Sum([1000000, 2000000, 3000000, 4000000, 5000000], 5), 15000000)

    def test_empty_array(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("1, 2, 3, 4, 5", 5)

        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3, 4, 5], "5")

        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3, 4, 5], -1)
