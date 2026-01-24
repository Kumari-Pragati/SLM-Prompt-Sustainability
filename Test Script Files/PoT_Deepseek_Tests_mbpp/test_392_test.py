import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 2)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)
        self.assertEqual(get_max_sum(6), 6)
        self.assertEqual(get_max_sum(7), 7)
        self.assertEqual(get_max_sum(8), 8)
        self.assertEqual(get_max_sum(9), 9)
        self.assertEqual(get_max_sum(10), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(11), 11)
        self.assertEqual(get_max_sum(12), 12)
        self.assertEqual(get_max_sum(13), 13)
        self.assertEqual(get_max_sum(14), 14)
        self.assertEqual(get_max_sum(15), 15)
        self.assertEqual(get_max_sum(16), 16)
        self.assertEqual(get_max_sum(17), 17)
        self.assertEqual(get_max_sum(18), 18)
        self.assertEqual(get_max_sum(19), 19)
        self.assertEqual(get_max_sum(20), 20)

    def test_corner_cases(self):
        self.assertEqual(get_max_sum(21), 21)
        self.assertEqual(get_max_sum(22), 22)
        self.assertEqual(get_max_sum(23), 23)
        self.assertEqual(get_max_sum(24), 24)
        self.assertEqual(get_max_sum(25), 25)
        self.assertEqual(get_max_sum(26), 26)
        self.assertEqual(get_max_sum(27), 27)
        self.assertEqual(get_max_sum(28), 28)
        self.assertEqual(get_max_sum(29), 29)
        self.assertEqual(get_max_sum(30), 30)
