import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_no_of_ways(4, 2), 5)
        self.assertEqual(count_no_of_ways(5, 2), 12)
        self.assertEqual(count_no_of_ways(6, 2), 22)
        self.assertEqual(count_no_of_ways(7, 2), 36)
        self.assertEqual(count_no_of_ways(8, 2), 57)

    def test_edge_case_small_n(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 2)
        self.assertEqual(count_no_of_ways(3, 1), 3)

    def test_edge_case_small_k(self):
        self.assertEqual(count_no_of_ways(4, 1), 4)
        self.assertEqual(count_no_of_ways(4, 0), 1)

    def test_edge_case_large_n(self):
        self.assertEqual(count_no_of_ways(100, 2), 184756)

    def test_invalid_input_negative_n(self):
        self.assertRaises(ValueError, count_no_of_ways, -1, 2)

    def test_invalid_input_negative_k(self):
        self.assertRaises(ValueError, count_no_of_ways, 4, -1)
