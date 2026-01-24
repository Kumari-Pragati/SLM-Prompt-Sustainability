import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_edge_cases(self):
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([1], []), [])
        self.assertEqual(mul_list([], [1]), [])

    def test_boundary_cases(self):
        self.assertEqual(mul_list([1, 2], [3, 4]), [3, 8])
        self.assertEqual(mul_list([1], [2, 3]), [2, 6])

    def test_special_cases(self):
        self.assertEqual(mul_list([-1, 1], [2, 3]), [-2, 3])
        self.assertEqual(mul_list([1, 2, 3], [-4, -5, -6]), [-4, -10, -18])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            mul_list(None, [1, 2, 3])
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], None)
