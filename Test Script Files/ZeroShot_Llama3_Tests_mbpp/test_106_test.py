import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_add_lists(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))
        self.assertEqual(add_lists([1, 2, 3, 4, 5], (6, 7, 8, 9, 10)), (6, 7, 8, 9, 10, 1, 2, 3, 4, 5))
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))
        self.assertEqual(add_lists([1, 2, 3], ()), ())
        self.assertEqual(add_lists([1, 2, 3, 4, 5, 6], (7, 8, 9, 10, 11, 12)), (7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6))

    def test_add_lists_empty(self):
        self.assertEqual(add_lists([], ()), ())
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))
