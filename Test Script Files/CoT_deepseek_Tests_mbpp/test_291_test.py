import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no_of_ways(3, 2), 4)

    def test_large_number(self):
        self.assertEqual(count_no_of_ways(10, 3), 2704)

    def test_small_number(self):
        self.assertEqual(count_no_of_ways(1, 5), 5)

    def test_zero_number(self):
        self.assertEqual(count_no_of_ways(0, 3), 0)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            count_no_of_ways(-1, 3)

    def test_negative_k(self):
        with self.assertRaises(Exception):
            count_no_of_ways(3, -1)

    def test_zero_k(self):
        with self.assertRaises(Exception):
            count_no_of_ways(3, 0)
