import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):

    def test_add_list(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([-1, 0, 1], [1, 2, 3]), [0, 2, 4])
        self.assertEqual(add_list([1, 2, 3], [-1, -2, -3]), [0, 0, 0])
        self.assertEqual(add_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(add_list([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(add_list([1, 2, 3], [1, 2, 3]), [2, 4, 6])
        self.assertEqual(add_list([-1, -2, -3], [-1, -2, -3]), [-2, -4, -6])
        self.assertEqual(add_list([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [2, 4, 6, 8, 10])
        self.assertEqual(add_list([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]), [2, 4, 6, 8, 10, 12])
