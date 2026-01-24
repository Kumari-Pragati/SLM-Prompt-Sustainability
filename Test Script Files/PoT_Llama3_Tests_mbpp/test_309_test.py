import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum(5, 3), 5)

    def test_typical_case2(self):
        self.assertEqual(maximum(3, 5), 5)

    def test_edge_case_equal(self):
        self.assertEqual(maximum(5, 5), 5)

    def test_edge_case_negative(self):
        self.assertEqual(maximum(-5, -3), -3)

    def test_edge_case_zero(self):
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_case_negative_zero(self):
        self.assertEqual(maximum(-5, 0), 0)

    def test_edge_case_zero_negative(self):
        self.assertEqual(maximum(0, -5), 0)

    def test_edge_case_negative_negative(self):
        self.assertEqual(maximum(-5, -3), -3)
