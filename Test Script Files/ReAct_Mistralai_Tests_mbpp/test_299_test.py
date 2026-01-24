import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_empty_list(self):
        """Test if function returns correct result for empty list"""
        self.assertIsNone(max_aggregate([]))

    def test_single_entry(self):
        """Test if function returns correct result for single entry"""
        self.assertEqual(max_aggregate([('Alice', 85)]), ('Alice', 85))

    def test_multiple_entries_same_name(self):
        """Test if function returns correct result for multiple entries with same name"""
        self.assertEqual(max_aggregate([('Alice', 85), ('Alice', 90)]), ('Alice', 90))

    def test_multiple_entries_different_names(self):
        """Test if function returns correct result for multiple entries with different names"""
        self.assertEqual(max_aggregate([('Alice', 85), ('Bob', 90)]), ('Bob', 90))

    def test_negative_marks(self):
        """Test if function handles negative marks correctly"""
        self.assertEqual(max_aggregate([('Alice', -10), ('Bob', 90)]), ('Bob', 90))

    def test_zero_marks(self):
        """Test if function handles zero marks correctly"""
        self.assertEqual(max_aggregate([('Alice', 0), ('Bob', 90)]), ('Bob', 90))
