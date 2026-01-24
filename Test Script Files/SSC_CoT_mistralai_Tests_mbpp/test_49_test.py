import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_normal(self):
        self.assertListEqual(specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [1, 4, 7])
        self.assertListEqual(specified_element([[1], [2], [3]], 0), [1, 2, 3])
        self.assertListEqual(specified_element([[1, 2], [3, 4]], 1), [2, 4])

    def test_edge_and_boundary(self):
        self.assertListEqual(specified_element([], 0), [])
        self.assertListEqual(specified_element([[1]], 0), [1])
        self.assertListEqual(specified_element([[1], [2]], 2), [])
        self.assertListEqual(specified_element([[1], [2]], 3), [])
        self.assertListEqual(specified_element([[1], [2]], -1), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, specified_element, [1, 2, 3], 'N')
        self.assertRaises(TypeError, specified_element, [1, 2, 3], 4.5)
        self.assertRaises(TypeError, specified_element, [1, 2, 3], -1)
