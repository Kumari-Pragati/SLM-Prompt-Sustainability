import unittest
from mbpp_299_code import defaultdict
from twenty_nine_nine import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_aggregate([]))

    def test_single_element(self):
        self.assertEqual(max_aggregate([('Alice', 80)]), ('Alice', 80))

    def test_multiple_elements(self):
        self.assertEqual(max_aggregate([('Alice', 80), ('Bob', 75), ('Alice', 85)]), ('Alice', 165))

    def test_duplicate_names(self):
        self.assertEqual(max_aggregate([('Alice', 80), ('Alice', 85), ('Bob', 75)]), ('Alice', 165))

    def test_negative_marks(self):
        self.assertEqual(max_aggregate([('Alice', -10), ('Bob', 75)]), ('Bob', 75))

    def test_zero_marks(self):
        self.assertEqual(max_aggregate([('Alice', 0), ('Bob', 75)]), ('Bob', 75))
