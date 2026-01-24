import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 2, 6), [[2, 3], [4, 5]])

    def test_edge_case_leftrange(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 1, 6), [[1, 2], [3, 4], [5, 6]])

    def test_edge_case_rightrange(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 2, 6), [[2, 3], [4, 5], [5, 6]])

    def test_boundary_case(self):
        self.assertEqual(remove_list_range([[2, 3], [4, 5]], 2, 5), [[2, 3], [4, 5]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_list_range([1, 2, 3], 1, 2)
