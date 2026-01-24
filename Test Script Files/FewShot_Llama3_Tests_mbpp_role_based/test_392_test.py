import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):
    def test_small_input(self):
        self.assertEqual(get_max_sum(5), 7)

    def test_medium_input(self):
        self.assertEqual(get_max_sum(10), 17)

    def test_large_input(self):
        self.assertEqual(get_max_sum(15), 26)

    def test_edge_case_zero(self):
        self.assertEqual(get_max_sum(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(get_max_sum(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(get_max_sum(2), 2)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            get_max_sum('a')
