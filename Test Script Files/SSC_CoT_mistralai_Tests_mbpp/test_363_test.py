import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(add_K_element([[1, 2], [3, 4]], 1), [[2, 3], [4, 5]])
        self.assertListEqual(add_K_element([[-1, -2], [-3, -4]], -1), [[0, 0], [2, 3]])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(add_K_element([], 0), [[]])
        self.assertListEqual(add_K_element([[0]], 0), [([0])])
        self.assertListEqual(add_K_element([[0]], 1), [([1])])
        self.assertListEqual(add_K_element([[1]], 0), [([1])])

    def test_negative_K(self):
        self.assertListEqual(add_K_element([[1, 2], [3, 4]], -1), [[0, 1], [2, 3]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_K_element('test', 1)
        with self.assertRaises(TypeError):
            add_K_element([1], 'test')
