import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Extract([[1, 2], [3, 4], [5, 6]]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([[7, 8]]), [7])

    def test_list_with_single_element_sublists(self):
        self.assertEqual(Extract([[9, 10], [11, 12], [13, 14]]), [9, 11, 13])

    def test_list_with_multiple_element_sublists(self):
        self.assertEqual(Extract([[15, 16, 17], [18, 19, 20], [21, 22, 23]]), [15, 18, 21])

    def test_list_with_mixed_length_sublists(self):
        self.assertEqual(Extract([[24, 25], [26, 27, 28], [29, 30, 31, 32]]), [24, 26, 29])
