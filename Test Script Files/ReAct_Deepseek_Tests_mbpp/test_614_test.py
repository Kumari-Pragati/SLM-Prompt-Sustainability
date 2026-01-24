import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4]]), 10)

    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_number(self):
        self.assertEqual(cummulative_sum([[5]]), 5)

    def test_single_sublist(self):
        self.assertEqual(cummulative_sum([[1, 2, 3]]), 6)

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([[1, -2], [-3, 4]]), 2)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            cummulative_sum([[1, '2'], [3, 4]])

    def test_non_list_elements(self):
        with self.assertRaises(TypeError):
            cummulative_sum([1, 2, 3])

    def test_empty_sublists(self):
        self.assertEqual(cummulative_sum([[], []]), 0)
