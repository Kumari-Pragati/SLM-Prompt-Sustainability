import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3], 2), [(3, 3), (2, 2)])

    def test_single_element(self):
        self.assertEqual(most_common_elem([1], 1), [(1, 1)])

    def test_empty_list(self):
        self.assertEqual(most_common_elem([], 1), [])

    def test_large_number_of_elements(self):
        self.assertEqual(most_common_elem(list(range(1, 10001)), 10), [(1, 10000)])

    def test_most_common_elem_with_multiple_most_common(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3), [(4, 4), (3, 3), (2, 2)])

    def test_most_common_elem_with_less_elements_than_requested(self):
        self.assertEqual(most_common_elem([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 6), [(4, 4), (3, 3), (2, 2), (1, 1)])

    def test_most_common_elem_with_negative_numbers(self):
        self.assertEqual(most_common_elem([-1, -2, -2, -3, -3, -3], 2), [(-3, 3), (-2, 2)])

    def test_most_common_elem_with_zero(self):
        self.assertEqual(most_common_elem([0, 0, 1, 1, 2, 2], 2), [(0, 2), (2, 2)])

    def test_most_common_elem_with_invalid_input(self):
        with self.assertRaises(TypeError):
            most_common_elem("not a list", 1)
