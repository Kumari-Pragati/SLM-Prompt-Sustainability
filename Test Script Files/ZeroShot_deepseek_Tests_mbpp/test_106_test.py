import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_add_lists(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))
        self.assertEqual(add_lists(['a', 'b', 'c'], ('d', 'e', 'f')), ('d', 'e', 'f', 'a', 'b', 'c'))
        self.assertEqual(add_lists([], ()), ())
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))
