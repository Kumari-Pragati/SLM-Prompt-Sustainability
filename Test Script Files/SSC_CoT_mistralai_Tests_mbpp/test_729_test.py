import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(add_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(add_list([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(add_list([1, 2, 3], []), [1, 2, 3])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(add_list([0, 0, 0], [0, 0, 0]), [0, 0, 0])
        self.assertEqual(add_list([-1, 0, 1], [-1, 0, 1]), [0, 0, 2])
        self.assertEqual(add_list([1000000000000, 2, 3], [4, 5, 6]), [1000000000002, 7, 9])

    def test_special_cases(self):
        self.assertEqual(add_list([1.5, 2.5, 3.5], [4.5, 5.5, 6.5]), [6.0, 8.0, 10.0])
        self.assertEqual(add_list([1, '2', 3], [4, 5, 6]), [5, 7, 9])
