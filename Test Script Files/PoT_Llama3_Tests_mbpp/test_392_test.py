import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_max_sum(5), 7)

    def test_edge_case(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 2)

    def test_boundary_case(self):
        self.assertEqual(get_max_sum(4), 3)
        self.assertEqual(get_max_sum(5), 7)
        self.assertEqual(get_max_sum(6), 8)

    def test_tricky_case(self):
        self.assertEqual(get_max_sum(10), 17)
