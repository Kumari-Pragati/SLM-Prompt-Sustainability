import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no_of_ways(4, 2), 5)
        self.assertEqual(count_no_of_ways(5, 2), 10)
        self.assertEqual(count_no_of_ways(6, 2), 19)

    def test_edge_case_small_n(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 2)

    def test_edge_case_small_k(self):
        self.assertEqual(count_no_of_ways(4, 1), 3)
        self.assertEqual(count_no_of_ways(5, 1), 4)

    def test_edge_case_large_k(self):
        self.assertEqual(count_no_of_ways(4, 3), 1)
        self.assertEqual(count_no_of_ways(5, 3), 2)

    def test_error_case_negative_n(self):
        self.assertRaises(ValueError, count_no_of_ways, -1, 2)

    def test_error_case_negative_k(self):
        self.assertRaises(ValueError, count_no_of_ways, 4, -1)
