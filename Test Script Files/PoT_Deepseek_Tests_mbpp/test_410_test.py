import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_val([5, 3, 9, 1]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(min_val([7]), 7)

    def test_edge_case_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(min_val([-5, -3, -9, -1]), -9)

    def test_boundary_case_large_numbers(self):
        self.assertEqual(min_val([1000000, 2000000, 3000000]), 1000000)

    def test_corner_case_mixed_types(self):
        self.assertEqual(min_val([5, '3', 9, 1]), 1)

    def test_corner_case_non_integer_elements(self):
        self.assertEqual(min_val(['5', '3', '9', '1']), '1')

    def test_corner_case_all_non_integer_elements(self):
        self.assertIsNone(min_val(['five', 'three', 'nine', 'one']))
