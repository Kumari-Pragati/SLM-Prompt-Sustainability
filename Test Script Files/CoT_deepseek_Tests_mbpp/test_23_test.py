import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 36)

    def test_single_element(self):
        self.assertEqual(maximum_Sum([[5]]), 5)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -6)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_empty_sublists(self):
        self.assertEqual(maximum_Sum([[], [], []]), -100000)

    def test_single_sublist(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_Sum([[1, -2, 3], [-4, 5, -6], [7, -8, 9]]), 13)

    def test_large_numbers(self):
        self.assertEqual(maximum_Sum([[10000, 20000, 30000], [40000, 50000, 60000], [70000, 80000, 90000]]), 270000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_Sum("not a list")

        with self.assertRaises(TypeError):
            maximum_Sum([1, 2, 3])

        with self.assertRaises(TypeError):
            maximum_Sum([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
