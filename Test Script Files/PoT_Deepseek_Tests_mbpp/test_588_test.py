import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(big_diff([5]), 0)

    def test_boundary_case_min_max(self):
        self.assertEqual(big_diff([-100, 100]), 200)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(big_diff([-1, -2, -3]), 2)

    def test_corner_case_duplicate_min_max(self):
        self.assertEqual(big_diff([10, 10, 10]), 0)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(ValueError):
            big_diff([])

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            big_diff([1, 2, '3'])
