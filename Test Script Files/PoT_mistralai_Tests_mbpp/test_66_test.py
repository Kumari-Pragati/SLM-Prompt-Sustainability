import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)
        self.assertEqual(pos_count([]), 0)
        self.assertEqual(pos_count([0, -1, 2, -3, 4]), 3)

    def test_zero(self):
        self.assertEqual(pos_count([0]), 1)

    def test_negative_numbers(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)
