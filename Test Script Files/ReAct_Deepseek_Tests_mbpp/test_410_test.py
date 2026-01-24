import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_val([5, 3, 9, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_list_with_non_integers(self):
        self.assertEqual(min_val([5, 'a', 9, 1]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(min_val([5, 3, 9, 1, 1]), 1)

    def test_single_integer(self):
        self.assertEqual(min_val([5]), 5)

    def test_all_integers_same_value(self):
        self.assertEqual(min_val([5, 5, 5, 5]), 5)

    def test_list_with_negative_integers(self):
        self.assertEqual(min_val([-5, -3, -9, -1]), -9)

    def test_list_with_zero(self):
        self.assertEqual(min_val([0, 3, 9, 1]), 0)
