import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(pos_count([1, 2, 3]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(pos_count([-1, 0, 1, -2, 3]), 3)
