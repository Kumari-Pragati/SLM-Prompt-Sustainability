import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_mul_list(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])
        self.assertEqual(mul_list([-1, 2, 3], [4, -5, 6]), [-4, -10, 18])
        self.assertEqual(mul_list([1, 2, 3], [-4, 5, -6]), [-4, 10, -18])
        self.assertEqual(mul_list([-1, -2, -3], [-4, -5, -6]), [4, 10, 18])
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([1, 2, 3], []), [])
        self.assertEqual(mul_list([], [1, 2, 3]), [])

    def test_mul_list_empty_input(self):
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([], [1, 2, 3]), [])
        self.assertEqual(mul_list([1, 2, 3], []), [])
