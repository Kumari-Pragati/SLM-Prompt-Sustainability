import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(pos_count([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(pos_count([1, -2, 3, -4, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_zero(self):
        self.assertEqual(pos_count([0]), 1)

    def test_floats(self):
        self.assertEqual(pos_count([0.5, -2.3, 3.14]), 2)

    def test_invalid_input(self):
        self.assertRaises(TypeError, pos_count, "not a list")
