import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_all_positive_list(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)

    def test_all_negative_list(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_mixed_list(self):
        self.assertEqual(pos_count([-1, 0, 1, -2, 3]), 3)

    def test_zero_list(self):
        self.assertEqual(pos_count([0]), 1)

    def test_large_positive_list(self):
        self.assertEqual(pos_count(list(range(1000))), 999)

    def test_large_negative_list(self):
        self.assertEqual(pos_count(list(range(-1000, -1, -1))), 0)

    def test_list_with_float(self):
        self.assertEqual(pos_count([-0.5, 0, 1.5]), 2)
