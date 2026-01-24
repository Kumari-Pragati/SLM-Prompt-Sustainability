import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):
    def test_simple_positive_numbers(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)

    def test_simple_negative_numbers(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(pos_count([-1, 0, 1]), 2)

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_single_positive_number(self):
        self.assertEqual(pos_count([5]), 1)

    def test_single_negative_number(self):
        self.assertEqual(pos_count([-5]), 0)

    def test_single_zero(self):
        self.assertEqual(pos_count([0]), 0)
