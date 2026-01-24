import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_single_positive(self):
        self.assertEqual(pos_count([1]), 1)

    def test_single_negative(self):
        self.assertEqual(pos_count([-1]), 0)

    def test_multiple_positive(self):
        self.assertEqual(pos_count([1, 2, 3]), 3)

    def test_multiple_negative(self):
        self.assertEqual(pos_count([-1, -2, -3]), 0)

    def test_mixed_positive_negative(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 3)

    def test_all_positive(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)

    def test_all_negative(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_list_with_zero(self):
        self.assertEqual(pos_count([0, 1, 2, 3, 4]), 4)
