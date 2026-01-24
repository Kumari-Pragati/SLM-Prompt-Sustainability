import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(jacobsthal_num(0), 0)
        self.assertEqual(jacobsthal_num(1), 1)
        self.assertEqual(jacobsthal_num(2), 2)
        self.assertEqual(jacobsthal_num(3), 5)
        self.assertEqual(jacobsthal_num(4), 10)
        self.assertEqual(jacobsthal_num(5), 21)

    def test_boundary_conditions(self):
        self.assertEqual(jacobsthal_num(6), 42)
        self.assertEqual(jacobsthal_num(7), 85)
        self.assertEqual(jacobsthal_num(8), 170)

    def test_negative_numbers(self):
        with self.assertRaises(IndexError):
            jacobsthal_num(-1)

    def test_large_numbers(self):
        self.assertEqual(jacobsthal_num(10), 1048575)
        self.assertEqual(jacobsthal_num(20), 1048575)
