import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -6)

    def test_edge_input(self):
        self.assertEqual(sum_negativenum([0]), 0)
        self.assertEqual(sum_negativenum([-0]), 0)
        self.assertEqual(sum_negativenum([-1]), -1)
        self.assertEqual(sum_negativenum([-2]), -2)
        self.assertEqual(sum_negativenum([-999999999]), -999999999)

    def test_boundary_input(self):
        self.assertEqual(sum_negativenum([-1, 0]), -1)
        self.assertEqual(sum_negativenum([0, -1]), -1)
        self.assertEqual(sum_negativenum([-1, 1]), 0)
        self.assertEqual(sum_negativenum([1, -1]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_negativenum(1.23)
        with self.assertRaises(TypeError):
            sum_negativenum("str")
        with self.assertRaises(TypeError):
            sum_negativenum(True)
        with self.assertRaises(TypeError):
            sum_negativenum(None)
