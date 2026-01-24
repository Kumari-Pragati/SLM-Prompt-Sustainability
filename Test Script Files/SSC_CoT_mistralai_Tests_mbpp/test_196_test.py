import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(remove_tuples([(1, 2, 3), (4, 5), (6, 7, 8, 9)], 3), [(4, 5), (6, 7, 8, 9)])
        self.assertListEqual(remove_tuples([(1, 2, 3), (4, 5), (6, 7, 8, 9)], 4), [(1, 2, 3), (4, 5)])

    def test_edge_input(self):
        self.assertListEqual(remove_tuples([(1, 2, 3)], 3), [])
        self.assertListEqual(remove_tuples([(1, 2, 3)], 1), [(1, 2, 3)])
        self.assertListEqual(remove_tuples([], 3), [])

    def test_boundary_input(self):
        self.assertListEqual(remove_tuples([(1, 2, 3), (1, 2), (1)], 3), [(1, 2)])
        self.assertListEqual(remove_tuples([(1, 2, 3), (1, 2), (1)], 1), [(1, 2, 3), (1, 2), (1)])
        self.assertListEqual(remove_tuples([(1, 2, 3), (1, 2), (1)], 0), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_tuples(1, 3)
        with self.assertRaises(TypeError):
            remove_tuples([1, 2, 3], "K")
