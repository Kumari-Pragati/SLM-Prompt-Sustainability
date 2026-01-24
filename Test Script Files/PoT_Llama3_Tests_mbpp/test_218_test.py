import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 20), 4)

    def test_edge_case_A_greater_than_B(self):
        self.assertEqual(min_Operations(20, 10), 4)

    def test_edge_case_A_equal_to_B(self):
        self.assertEqual(min_Operations(10, 10), 1)

    def test_edge_case_A_zero(self):
        self.assertEqual(min_Operations(0, 10), 0)

    def test_edge_case_B_zero(self):
        self.assertEqual(min_Operations(10, 0), 0)

    def test_edge_case_A_and_B_zero(self):
        self.assertEqual(min_Operations(0, 0), 0)

    def test_edge_case_A_negative(self):
        self.assertEqual(min_Operations(-10, 20), 4)

    def test_edge_case_B_negative(self):
        self.assertEqual(min_Operations(10, -20), 4)

    def test_edge_case_A_and_B_negative(self):
        self.assertEqual(min_Operations(-10, -20), 0)
