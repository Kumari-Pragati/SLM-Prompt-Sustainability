import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):

    def test_add_list(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([-1, 2, -3], [4, -5, 6]), [3, -3, 3])
        self.assertEqual(add_list([], []), [])
        self.assertEqual(add_list([1], [2]), [3])
        self.assertEqual(add_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), [7, 9, 11, 13, 15])
