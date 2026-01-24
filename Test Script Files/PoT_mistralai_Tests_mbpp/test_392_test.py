import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 2)
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)
        self.assertEqual(get_max_sum(6), 7)
        self.assertEqual(get_max_sum(7), 8)
        self.assertEqual(get_max_sum(8), 9)
        self.assertEqual(get_max_sum(9), 10)
        self.assertEqual(get_max_sum(10), 17)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(11), 20)
        self.assertEqual(get_max_sum(12), 24)
        self.assertEqual(get_max_sum(21), 68)
        self.assertEqual(get_max_sum(32), 105)
        self.assertEqual(get_max_sum(43), 167)
        self.assertEqual(get_max_sum(54), 242)
        self.assertEqual(get_max_sum(65), 330)
        self.assertEqual(get_max_sum(76), 433)
        self.assertEqual(get_max_sum(87), 556)
        self.assertEqual(get_max_sum(98), 693)
