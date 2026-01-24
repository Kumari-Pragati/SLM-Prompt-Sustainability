import unittest
from mbpp_291_code import count_no_of_ways

class TestCountNoOfWays(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_no_of_ways(4, 2), 5)
        self.assertEqual(count_no_of_ways(5, 2), 12)
        self.assertEqual(count_no_of_ways(6, 2), 22)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_no_of_ways(1, 1), 1)
        self.assertEqual(count_no_of_ways(2, 1), 2)
        self.assertEqual(count_no_of_ways(3, 1), 3)
        self.assertEqual(count_no_of_ways(4, 1), 6)
        self.assertEqual(count_no_of_ways(5, 1), 10)
        self.assertEqual(count_no_of_ways(6, 1), 15)
        self.assertEqual(count_no_of_ways(7, 1), 21)
        self.assertEqual(count_no_of_ways(8, 1), 28)
        self.assertEqual(count_no_of_ways(9, 1), 36)
        self.assertEqual(count_no_of_ways(10, 1), 45)
        self.assertEqual(count_no_of_ways(11, 1), 55)
        self.assertEqual(count_no_of_ways(12, 1), 66)
        self.assertEqual(count_no_of_ways(13, 1), 78)
        self.assertEqual(count_no_of_ways(14, 1), 91)
        self.assertEqual(count_no_of_ways(15, 1), 105)
        self.assertEqual(count_no_of_ways(16, 1), 120)
        self.assertEqual(count_no_of_ways(17, 1), 136)
        self.assertEqual(count_no_of_ways(18, 1), 153)
        self.assertEqual(count_no_of_ways(19, 1), 171)
        self.assertEqual(count_no_of_ways(20, 1), 190)

        self.assertEqual(count_no_of_ways(1, 2), 1)
        self.assertEqual(count_no_of_ways(2, 2), 2)
        self.assertEqual(count_no_of_ways(3, 2), 5)
        self.assertEqual(count_no_of_ways(4, 2), 12)
        self.assertEqual(count_no_of_ways(5, 2), 22)
        self.assertEqual(count_no_of_ways(6, 2), 35)
        self.assertEqual(count_no_of_ways(7, 2), 51)
        self.assertEqual(count_no_of_ways(8, 2), 70)
        self.assertEqual(count_no_of_ways(9, 2), 92)
        self.assertEqual(count_no_of_ways(10, 2), 118)
        self.assertEqual(count_no_of_ways(11, 2), 148)
        self.assertEqual(count_no_of_ways(12, 2), 180)
        self.assertEqual(count_no_of_ways(13, 2), 215)
        self.assertEqual(count_no_of_ways(14, 2), 253)
        self.assertEqual(count_no_of_ways(15, 2), 303)
        self.assertEqual(count_no_of_ways(16, 2), 359)
        self.assertEqual(count_no_of_ways(17, 2), 420)
        self.assertEqual(count_no_