import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([0], [0]), [0])
        self.assertEqual(add_list([], []), [])

    def test_edge_cases(self):
        self.assertEqual(add_list([1], []), [1])
        self.assertEqual(add_list([], [1]), [1])
        self.assertEqual(add_list([1], [2, 3]), [3, 4])
        self.assertEqual(add_list([2, 3], [1]), [3, 4])

    def test_boundary_values(self):
        self.assertEqual(add_list([sys.maxsize], [1]), [sys.maxsize + 1])
        self.assertEqual(add_list([sys.maxsize], [sys.maxsize]), [2 * sys.maxsize])
        self.assertEqual(add_list([-sys.maxsize], [-1]), [-sys.maxsize - 1])
        self.assertEqual(add_list([-sys.maxsize], [-sys.maxsize]), [0])
