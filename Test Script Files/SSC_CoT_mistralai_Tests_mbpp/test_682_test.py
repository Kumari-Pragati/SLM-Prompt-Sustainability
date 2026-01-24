import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])
        self.assertEqual(mul_list([0], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(mul_list([1, 0, 3], [4, 0, 5]), [0, 0, 15])

    def test_edge_cases(self):
        self.assertEqual(mul_list([], []), [])
        self.assertEqual(mul_list([1], []), [])
        self.assertEqual(mul_list([], [1]), [])

    def test_negative_numbers(self):
        self.assertEqual(mul_list([-1, 2, -3], [4, -5, 6]), [-4, 10, -18])
        self.assertEqual(mul_list([-1, 0, -3], [4, 0, -5]), [-0, 0, 15])

    def test_floats(self):
        self.assertListEqual(mul_list([1.5, 2.0, 3.5], [4.0, 5.0, 6.0]),
                              [6.0, 10.0, 21.0])
        self.assertListEqual(mul_list([0.0, 0.0, 0.0], [1.0, 2.0, 3.0]),
                              [0.0, 0.0, 0.0])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            mul_list('str', [1, 2, 3])
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], 'str')
