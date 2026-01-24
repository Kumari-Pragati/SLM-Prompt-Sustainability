import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, max_of_nth, [], 0)

    def test_single_element_list(self):
        self.assertEqual(max_of_nth([[1]], 0), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(max_of_nth([[1, 2], [3, 4]], 0), 3)
        self.assertEqual(max_of_nth([[1, 2], [3, 4]], 1), 2)
        self.assertEqual(max_of_nth([[1, 2], [3, 4]], 2), 4)

    def test_negative_index(self):
        self.assertRaises(IndexError, max_of_nth, [[1, 2], [3, 4]], -1)

    def test_invalid_index(self):
        self.assertRaises(IndexError, max_of_nth, [[1, 2], [3, 4]], 20)
