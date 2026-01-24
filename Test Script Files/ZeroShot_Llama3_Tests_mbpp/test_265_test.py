import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_list_split(self):
        self.assertEqual(list_split('123456', 2), ['12', '34', '56'])
        self.assertEqual(list_split('123456', 3), ['123', '456'])
        self.assertEqual(list_split('123456', 1), ['1', '2', '3', '4', '5', '6'])
        self.assertEqual(list_split('123456', 4), ['1234', '56'])
        self.assertEqual(list_split('123456', 5), ['12345', '6'])
        self.assertEqual(list_split('123456', 6), ['123456'])

    def test_list_split_empty_string(self):
        self.assertEqual(list_split('', 2), [])

    def test_list_split_step_zero(self):
        with self.assertRaises(ValueError):
            list_split('123456', 0)

    def test_list_split_step_negative(self):
        with self.assertRaises(ValueError):
            list_split('123456', -1)
