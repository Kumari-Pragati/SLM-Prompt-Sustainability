import unittest
from195_code import first

class TestFirstFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 4), 2)
        self.assertEqual(first([10, 20, 30, 40, 50], 30, 5), 2)

    def test_edge_case_left(self):
        self.assertEqual(first([1], 1, 0), 0)
        self.assertEqual(first([1, 2], 2, 1), 1)

    def test_edge_case_right(self):
        self.assertEqual(first([1, 2], 3, 2), -1)
        self.assertEqual(first([1, 2, 3], 4, 3), 3)

    def test_invalid_input_arr(self):
        self.assertRaises(TypeError, first, [1, 2], 3, -1)

    def test_invalid_input_x(self):
        self.assertRaises(TypeError, first, [1, 2], 'x', 3)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, first, [1, 2], 3, 'n')
