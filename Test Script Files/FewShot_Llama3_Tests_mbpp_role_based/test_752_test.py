import unittest
from mbpp_752_code import jacobsthal_num

class TestJacobsthalNum(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(jacobsthal_num(0), 0)

    def test_one(self):
        self.assertEqual(jacobsthal_num(1), 1)

    def test_small_numbers(self):
        self.assertEqual(jacobsthal_num(2), 1)
        self.assertEqual(jacobsthal_num(3), 2)
        self.assertEqual(jacobsthal_num(4), 4)

    def test_larger_numbers(self):
        self.assertEqual(jacobsthal_num(5), 7)
        self.assertEqual(jacobsthal_num(6), 11)
        self.assertEqual(jacobsthal_num(7), 18)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            jacobsthal_num('a')
