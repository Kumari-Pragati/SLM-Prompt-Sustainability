import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(add_lists([], ()), ())

    def test_mixed_input(self):
        self.assertEqual(add_lists([1, 'a', True], (2, 'b', False)), (2, 'b', False, 1, 'a', True))

    def test_large_input(self):
        test_list = list(range(1, 1001))
        test_tup = tuple(range(1001, 2001))
        self.assertEqual(add_lists(test_list, test_tup), test_tup + test_list)

    def test_negative_input(self):
        self.assertEqual(add_lists([-1, -2, -3], (-4, -5, -6)), (-4, -5, -6, -1, -2, -3))
