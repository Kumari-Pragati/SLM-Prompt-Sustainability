import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_of_nth([], 0))

    def test_single_element_list(self):
        self.assertEqual(max_of_nth([[1]], 0), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(max_of_nth([[1, 2], [3, 4], [5, 6]], 0), 5)
        self.assertEqual(max_of_nth([[1, 2], [3, 4], [5, 6]], 1), 6)

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: max_of_nth([[1, 2]], -1))

    def test_invalid_index(self):
        self.assertRaises(IndexError, lambda: max_of_nth([[1, 2]], 2))
