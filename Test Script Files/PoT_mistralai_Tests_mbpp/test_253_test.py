import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_edge_case_single_integer(self):
        self.assertEqual(count_integer([4]), 1)

    def test_edge_case_single_non_integer(self):
        self.assertEqual(count_integer([4.0]), 1)

    def test_edge_case_all_non_integers(self):
        self.assertEqual(count_integer([4.0, 'a', True]), 1)

    def test_corner_case_negative_integers(self):
        self.assertEqual(count_integer([-1, -2, -3]), 3)

    def test_corner_case_zero(self):
        self.assertEqual(count_integer([0]), 1)
