import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_difference(3), 22)
        self.assertEqual(sum_difference(5), 100)
        self.assertEqual(sum_difference(10), 385)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_difference(0), 0)
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(20), 1764)
        self.assertEqual(sum_difference(100), 338350)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_difference(-1)
