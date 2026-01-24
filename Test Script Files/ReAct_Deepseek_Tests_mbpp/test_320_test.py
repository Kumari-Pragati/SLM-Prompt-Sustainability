import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_difference(5), 110)

    def test_boundary_case_1(self):
        self.assertEqual(sum_difference(1), 0)

    def test_boundary_case_2(self):
        self.assertEqual(sum_difference(0), 0)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            sum_difference(-5)

    def test_large_number_case(self):
        self.assertEqual(sum_difference(100), 25164150)
