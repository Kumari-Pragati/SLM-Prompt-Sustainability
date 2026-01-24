import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty(self):
        self.assertEqual(first_odd([]), -1)

    def test_edge_case_single(self):
        self.assertEqual(first_odd([1]), 1)

    def test_edge_case_all_even(self):
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)

    def test_edge_case_all_odd(self):
        self.assertEqual(first_odd([1, 3, 5, 7]), 1)

    def test_edge_case_mixed(self):
        self.assertEqual(first_odd([2, 1, 4, 3, 6, 5]), 1)

    def test_edge_case_mixed_with_negative(self):
        self.assertEqual(first_odd([-2, 1, -4, 3, -6, 5]), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            first_odd("hello")
