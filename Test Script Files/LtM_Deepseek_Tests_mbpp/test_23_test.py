import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 36)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -6)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_single_element_in_list(self):
        self.assertEqual(maximum_Sum([[1]]), 1)

    def test_single_element_in_sublist(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4], [5, 6, 7]]), 21)

    def test_maximum_value(self):
        self.assertEqual(maximum_Sum([[99999, 99998, 99997], [99996, 99995, 99994], [99993, 99992, 99991]]), 299991)

    def test_minimum_value(self):
        self.assertEqual(maximum_Sum([[-99999, -99998, -99997], [-99996, -99995, -99994], [-99993, -99992, -99991]]), -99991)
