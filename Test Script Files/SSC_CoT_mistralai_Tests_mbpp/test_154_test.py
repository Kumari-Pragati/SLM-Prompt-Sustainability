import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(specified_element([[1, 2, 3], [4, 5, 6]], 1), [1, 4])
        self.assertEqual(specified_element([[1], [2], [3]], 0), [1, 2, 3])
        self.assertEqual(specified_element([[1, 2], [3, 4], [5, 6]], 1), [2, 4, 6])

    def test_edge_cases(self):
        self.assertEqual(specified_element([[1], [2]], 1), [2])
        self.assertEqual(specified_element([[1, 2, 3], [4, 5], [6]], 2), [3, 5])
        self.assertEqual(specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [3, 6, 9])

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: specified_element([[1, 2, 3], [4, 5, 6]], -1))
        self.assertRaises(IndexError, lambda: specified_element([[1, 2, 3]], -1))

    def test_empty_list(self):
        self.assertRaises(IndexError, lambda: specified_element([]))
        self.assertRaises(IndexError, lambda: specified_element([[]]))
        self.assertRaises(IndexError, lambda: specified_element([[1], []]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, lambda: specified_element('invalid', 0))
        self.assertRaises(TypeError, lambda: specified_element([1, 2, 3], 'invalid'))
