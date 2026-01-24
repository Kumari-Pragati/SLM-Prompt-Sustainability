import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_zero_ways(self):
        self.assertEqual(count_no_of_ways(0, 1), 1)

    def test_one_ways(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)

    def test_two_ways(self):
        self.assertEqual(count_no_of_ways(2, 1), 1)

    def test_three_ways(self):
        self.assertEqual(count_no_of_ways(3, 1), 1)

    def test_k_ways(self):
        self.assertEqual(count_no_of_ways(10, 1), 1)

    def test_n_k_ways(self):
        self.assertEqual(count_no_of_ways(10, 2), 121)

    def test_large_n_ways(self):
        self.assertEqual(count_no_of_ways(20, 3), 14930352)

    def test_large_k_ways(self):
        self.assertEqual(count_no_of_ways(20, 4), 14930352)

    def test_negative_n_ways(self):
        with self.assertRaises(ValueError):
            count_no_of_ways(-1, 1)

    def test_negative_k_ways(self):
        with self.assertRaises(ValueError):
            count_no_of_ways(10, -1)
