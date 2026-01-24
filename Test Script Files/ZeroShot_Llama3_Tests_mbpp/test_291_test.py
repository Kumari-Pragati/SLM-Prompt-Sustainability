import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_count_no_of_ways(self):
        self.assertEqual(count_no_of_ways(1, 2), 2)
        self.assertEqual(count_no_of_ways(2, 2), 4)
        self.assertEqual(count_no_of_ways(3, 2), 7)
        self.assertEqual(count_no_of_ways(4, 2), 13)
        self.assertEqual(count_no_of_ways(5, 2), 24)
        self.assertEqual(count_no_of_ways(6, 2), 44)
        self.assertEqual(count_no_of_ways(7, 2), 81)
        self.assertEqual(count_no_of_ways(8, 2), 149)
        self.assertEqual(count_no_of_ways(9, 2), 274)
        self.assertEqual(count_no_of_ways(10, 2), 504)

    def test_count_no_of_ways_negative(self):
        with self.assertRaises(ValueError):
            count_no_of_ways(-1, 2)
        with self.assertRaises(ValueError):
            count_no_of_ways(1, -2)
