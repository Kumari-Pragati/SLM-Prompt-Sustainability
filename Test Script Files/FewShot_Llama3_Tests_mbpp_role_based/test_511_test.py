import unittest
from mbpp_511_code import find_Min_Sum

class TestFind_Min_Sum(unittest.TestCase):
    def test_small_prime(self):
        self.assertEqual(find_Min_Sum(10), 8)

    def test_large_prime(self):
        self.assertEqual(find_Min_Sum(100), 44)

    def test_composite_number(self):
        self.assertEqual(find_Min_Sum(36), 17)

    def test_edge_case_one(self):
        self.assertEqual(find_Min_Sum(1), 1)

    def test_edge_case_zero(self):
        self.assertEqual(find_Min_Sum(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            find_Min_Sum(-10)
