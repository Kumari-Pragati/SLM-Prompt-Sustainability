import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 2)
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)
        self.assertEqual(get_max_sum(6), 6)
        self.assertEqual(get_max_sum(7), 7)
        self.assertEqual(get_max_sum(8), 8)
        self.assertEqual(get_max_sum(9), 9)
        self.assertEqual(get_max_sum(10), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(11), 10)
        self.assertEqual(get_max_sum(12), 11)
        self.assertEqual(get_max_sum(2147483647), 2147483647)

    def test_special_cases(self):
        self.assertEqual(get_max_sum(2), 2)
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)
        self.assertEqual(get_max_sum(6), 6)
        self.assertEqual(get_max_sum(7), 7)
        self.assertEqual(get_max_sum(8), 8)
        self.assertEqual(get_max_sum(9), 9)
        self.assertEqual(get_max_sum(10), 10)
        self.assertEqual(get_max_sum(11), 10)
        self.assertEqual(get_max_sum(12), 11)
        self.assertEqual(get_max_sum(13), 11)
        self.assertEqual(get_max_sum(14), 12)
        self.assertEqual(get_max_sum(15), 13)
        self.assertEqual(get_max_sum(16), 14)
        self.assertEqual(get_max_sum(17), 15)
        self.assertEqual(get_max_sum(18), 16)
        self.assertEqual(get_max_sum(19), 17)
        self.assertEqual(get_max_sum(20), 18)
