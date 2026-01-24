import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, max_of_nth, [], 0)

    def test_single_element_list(self):
        self.assertEqual(max_of_nth([[1]], 0), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(max_of_nth([[1], [2], [3]], 0), 3)
        self.assertEqual(max_of_nth([[1], [2], [3]], 1), 2)
        self.assertEqual(max_of_nth([[1], [2], [3]], 2), 1)

    def test_negative_index(self):
        self.assertRaises(IndexError, max_of_nth, [[1]], -1)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, max_of_nth, [[1]], len([[1]]) + 1)

    def test_list_with_non_numeric_elements(self):
        self.assertRaises(TypeError, max_of_nth, [[1, 'a'], [2, 'b'], [3, 'c']], 0)
