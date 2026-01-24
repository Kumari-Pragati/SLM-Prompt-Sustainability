import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_multi_list(self):
        rownum = 3
        colnum = 3
        result = multi_list(rownum, colnum)
        self.assertEqual(len(result), rownum)
        for row in range(rownum):
            self.assertEqual(len(result[row]), colnum)
            for col in range(colnum):
                self.assertEqual(result[row][col], row*col)

    def test_multi_list_zero_rows(self):
        rownum = 0
        colnum = 3
        result = multi_list(rownum, colnum)
        self.assertEqual(result, [])

    def test_multi_list_zero_cols(self):
        rownum = 3
        colnum = 0
        result = multi_list(rownum, colnum)
        self.assertEqual(result, [])

    def test_multi_list_zero_rows_zero_cols(self):
        rownum = 0
        colnum = 0
        result = multi_list(rownum, colnum)
        self.assertEqual(result, [])
