import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_empty_list(self):
        """Test for empty list"""
        result = multi_list(0, 0)
        self.assertEqual(result, [])

    def test_single_row_single_column(self):
        """Test for single row and single column"""
        result = multi_list(1, 1)
        self.assertEqual(result, [[0]])

    def test_single_row_multiple_columns(self):
        """Test for single row and multiple columns"""
        result = multi_list(1, 3)
        self.assertEqual(result, [[0], [1], [2], [3]])

    def test_multiple_rows_single_column(self):
        """Test for multiple rows and single column"""
        result = multi_list(3, 1)
        self.assertEqual(result, [[0], [1], [2], [3]])

    def test_multiple_rows_multiple_columns(self):
        """Test for multiple rows and multiple columns"""
        result = multi_list(3, 4)
        expected = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]
        self.assertEqual(result, expected)

    def test_negative_rownum(self):
        """Test for negative row number"""
        with self.assertRaises(ValueError):
            multi_list(-1, 1)

    def test_negative_colnum(self):
        """Test for negative column number"""
        with self.assertRaises(ValueError):
            multi_list(1, -1)
