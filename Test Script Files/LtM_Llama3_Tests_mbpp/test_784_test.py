import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(mul_even_odd([2, 3]), 6)
        self.assertEqual(mul_even_odd([4, 5]), 20)
        self.assertEqual(mul_even_odd([6, 7]), 42)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            mul_even_odd([])

    def test_single_element(self):
        self.assertEqual(mul_even_odd([2]), -1)
        self.assertEqual(mul_even_odd([3]), -1)

    def test_all_even(self):
        self.assertEqual(mul_even_odd([2, 4, 6]), 24)

    def test_all_odd(self):
        self.assertEqual(mul_even_odd([1, 3, 5]), -1)

    def test_mixed(self):
        self.assertEqual(mul_even_odd([2, 3, 4, 5]), 60)
