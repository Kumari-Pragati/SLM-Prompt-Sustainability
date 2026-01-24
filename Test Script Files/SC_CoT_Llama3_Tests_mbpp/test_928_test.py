import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_edge_case_yyyy_mm_dd(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_edge_case_dd_mm_yyyy(self):
        self.assertEqual(change_date_format('25-07-2022'), '25-07-2022')

    def test_edge_case_mm_dd_yyyy(self):
        self.assertEqual(change_date_format('07-25-2022'), '25-07-2022')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            change_date_format('abc')

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            change_date_format(None)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            change_date_format('')

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            change_date_format(123)
