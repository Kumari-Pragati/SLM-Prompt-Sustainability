import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_count_no_of_ways_with_small_values(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 1)
        self.assertEqual(count_no_of_ways(2, 2), 1)
        self.assertEqual(count_no_of_ways(3, 1), 2)
        self.assertEqual(count_no_of_ways(3, 2), 2)
        self.assertEqual(count_no_of_ways(4, 1), 3)
        self.assertEqual(count_no_of_ways(4, 2), 5)
        self.assertEqual(count_no_of_ways(4, 3), 4)

    def test_count_no_of_ways_with_large_values(self):
        self.assertEqual(count_no_of_ways(10, 2), 55)
        self.assertEqual(count_no_of_ways(20, 2), 2110)
        self.assertEqual(count_no_of_ways(30, 2), 66860)
        self.assertEqual(count_no_of_ways(40, 2), 1881360)
        self.assertEqual(count_no_of_ways(50, 2), 49157800)
