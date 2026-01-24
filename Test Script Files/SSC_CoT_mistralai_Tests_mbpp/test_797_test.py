import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(sum_in_Range(1, 5), 6)
        self.assertEqual(sum_in_Range(10, 20), 91)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_in_Range(0, 1), 0)
        self.assertEqual(sum_in_Range(5, 5), 0)
        self.assertEqual(sum_in_Range(21, 21), 0)
        self.assertEqual(sum_in_Range(-1, 1), 0)
        self.assertEqual(sum_in_Range(1, -1), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_in_Range(-1, 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_in_Range('a', 'b')
        with self.assertRaises(TypeError):
            sum_in_Range(1.5, 2.5)
