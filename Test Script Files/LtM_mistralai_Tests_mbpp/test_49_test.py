import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(specified_element([[1, 2], [3, 4]], 0), [1, 3])
        self.assertListEqual(specified_element([[1, 2], [3, 4]], 1), [2, 4])

    def test_edge_and_boundary(self):
        self.assertListEqual(specified_element([], 0), [])
        self.assertListEqual(specified_element([[1], [2]], 1), [1, 2])
        self.assertListEqual(specified_element([[1], [2]], 2), [])

    def test_complex(self):
        self.assertListEqual(specified_element([[1, 2], [3, 4], [5, 6]], 2), [4, 6])
        self.assertListEqual(specified_element([[1, 2], [3, 4], [5, 6]], -1), [1, 3])
        self.assertListEqual(specified_element([[1, 2], [3, 4], [5, 6]], len([[1, 2], [3, 4], [5, 6]])), [5, 6])
