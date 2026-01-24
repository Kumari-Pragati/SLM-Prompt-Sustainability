import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 5)

    def test_single_element(self):
        self.assertEqual(max_difference([(1, 1)]), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_difference([(-1, 1), (2, -2), (3, -3)]), 5)

    def test_zero_difference(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_difference([])

    def test_single_tuple(self):
        with self.assertRaises(ValueError):
            max_difference([(1, 2, 3)])

    def test_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            max_difference([(1, '2'), (3, 4)])
