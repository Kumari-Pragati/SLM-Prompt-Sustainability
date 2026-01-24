import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_count_no_of_ways(self):
        self.assertEqual(count_no_of_ways(1, 2), 2)
        self.assertEqual(count_no_of_ways(2, 2), 4)
        self.assertEqual(count_no_of_ways(3, 2), 8)
        self.assertEqual(count_no_of_ways(4, 2), 16)
        self.assertEqual(count_no_of_ways(5, 2), 30)
        self.assertEqual(count_no_of_ways(6, 2), 54)
        self.assertEqual(count_no_of_ways(7, 2), 94)
        self.assertEqual(count_no_of_ways(8, 2), 166)
        self.assertEqual(count_no_of_ways(9, 2), 290)
        self.assertEqual(count_no_of_ways(10, 2), 504)
