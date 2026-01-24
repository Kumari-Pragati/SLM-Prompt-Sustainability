import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(maximum_Sum([[1]]), 1)
        self.assertEqual(maximum_Sum([[-1]]), -1)

    def test_multiple_elements_list(self):
        self.assertEqual(maximum_Sum([[1, 2], [3, 4], [5, 6]]), 15)
        self.assertEqual(maximum_Sum([[-1, -2], [-3, -4], [-5, -6]]), -15)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, 2], [-3, 4], [-5, 6]]), 6)

    def test_zero(self):
        self.assertEqual(maximum_Sum([[0], [0, 0], [0, 0, 0]]), 0)

    def test_large_numbers(self):
        self.assertEqual(maximum_Sum([[1000000, 2], [3, 4000000], [5, 6000000]]), 6000006)
