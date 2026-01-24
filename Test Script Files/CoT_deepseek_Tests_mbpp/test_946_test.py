import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2), [(4, 4), (3, 3)])

    def test_single_most_common(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1), [(4, 4)])

    def test_empty_list(self):
        self.assertEqual(most_common_elem([], 2), [])

    def test_negative_integers(self):
        self.assertEqual(most_common_elem([-1, -2, -2, -3, -3, -3, -4, -4, -4, -4], 2), [(-4, -4), (-3, -3)])

    def test_string_elements(self):
        self.assertEqual(most_common_elem(['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd'], 2), [('d', 4), ('c', 3)])

    def test_large_input(self):
        self.assertEqual(most_common_elem(list(range(1, 10001)), 10), [(1, 10000)])

    def test_a_greater_than_length(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 11), [(4, 4), (3, 3), (2, 2), (1, 1)])

    def test_a_equals_zero(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 0), [])

    def test_a_less_than_zero(self):
        with self.assertRaises(ValueError):
            most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], -1)
