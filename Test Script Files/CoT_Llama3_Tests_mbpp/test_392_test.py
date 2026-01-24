import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_get_max_sum_typical(self):
        self.assertEqual(get_max_sum(10), 17)

    def test_get_max_sum_edge(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 1)
        self.assertEqual(get_max_sum(4), 2)
        self.assertEqual(get_max_sum(5), 3)

    def test_get_max_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            get_max_sum('a')

    def test_get_max_sum_negative_input(self):
        with self.assertRaises(TypeError):
            get_max_sum(-1)

    def test_get_max_sum_zero_input(self):
        self.assertEqual(get_max_sum(0), 0)
