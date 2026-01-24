import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 5), 2)
        self.assertEqual(first([6, 7, 8, 9, 10], 7, 10), 4)
        self.assertEqual(first([11, 12, 13, 14, 15], 13, 15), 3)

    def test_edge_case_start(self):
        self.assertEqual(first([1], 1, 1), 0)
        self.assertEqual(first([1, 2], 2, 2), 1)
        self.assertEqual(first([1, 2, 3], 3, 3), 2)

    def test_edge_case_end(self):
        self.assertEqual(first([1, 2, 3], 1, 3), -1)
        self.assertEqual(first([4, 5], 5, 2), 1)
        self.assertEqual(first([6, 7], 7, 2), -1)

    def test_boundary_case_low(self):
        self.assertEqual(first([1, 2], 1, 1), 0)

    def test_boundary_case_high(self):
        self.assertEqual(first([1, 2], 2, 2), 1)

    def test_invalid_input_arr(self):
        self.assertRaises(TypeError, first, [1, 2], 3, -1)

    def test_invalid_input_x(self):
        self.assertRaises(TypeError, first, [1, 2], 'x', 3)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, first, [1, 2], 3, -1)
