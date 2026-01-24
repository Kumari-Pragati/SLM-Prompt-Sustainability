import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])
        self.assertEqual(mul_list([0], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(mul_list([1, 0, 3], [4, 0, 5]), [0, 0, 15])

    def test_edge_cases(self):
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([1], []), [])
        self.assertEqual(mul_list([], [1]), [])

    def test_boundary_values(self):
        self.assertEqual(mul_list([sys.maxsize], [1]), [sys.maxsize])
        self.assertEqual(mul_list([1], [sys.maxsize]), [sys.maxsize])
        self.assertEqual(mul_list([sys.maxsize], [sys.maxsize]), [sys.maxsize])

    def test_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, -3], [-4, -5, 6]), [4, -20, -18])
        self.assertEqual(mul_list([0, -1, 0], [-1, 0, 1]), [0, 0, 0])
        self.assertEqual(mul_list([-1, 0, -3], [1, 0, -1]), [0, 0, 3])
