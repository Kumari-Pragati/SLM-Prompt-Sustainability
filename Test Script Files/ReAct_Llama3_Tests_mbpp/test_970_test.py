import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_two(2, 4), 2)

    def test_edge_case_equal(self):
        self.assertEqual(min_of_two(2, 2), 2)

    def test_edge_case_negative(self):
        self.assertEqual(min_of_two(-1, -2), -2)

    def test_edge_case_zero(self):
        self.assertEqual(min_of_two(0, 0), 0)

    def test_edge_case_negative_zero(self):
        self.assertEqual(min_of_two(-1, 0), -1)

    def test_edge_case_zero_negative(self):
        self.assertEqual(min_of_two(0, -1), 0)

    def test_edge_case_negative_positive(self):
        self.assertEqual(min_of_two(-1, 2), -1)

    def test_edge_case_positive_negative(self):
        self.assertEqual(min_of_two(2, -1), -1)
