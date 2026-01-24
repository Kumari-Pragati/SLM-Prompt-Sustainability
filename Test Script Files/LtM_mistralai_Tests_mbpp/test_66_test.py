import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):
    def test_simple_positive_list(self):
        self.assertEqual(pos_count([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_all_negative_list(self):
        self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_min_value(self):
        self.assertEqual(pos_count([-1 * 2**31]), 1)

    def test_max_value(self):
        self.assertEqual(pos_count([2**31 - 1]), 1)

    def test_mixed_list(self):
        self.assertEqual(pos_count([-1, 0, 1, -2, 3]), 3)
