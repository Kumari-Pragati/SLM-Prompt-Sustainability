import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_single_element_list(self):
        self.assertEqual(left_insertion([1], 1), 0)
        self.assertEqual(left_insertion([1], 2), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(left_insertion([1, 2, 3], 1), 0)
        self.assertEqual(left_insertion([1, 2, 3], 2), 1)
        self.assertEqual(left_insertion([1, 2, 3], 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(left_insertion([5, 3, -2, -5], -5), 0)
        self.assertEqual(left_insertion([5, 3, -2, -5], -2), 2)
        self.assertEqual(left_insertion([5, 3, -2, -5], 3), 3)

    def test_floats(self):
        self.assertEqual(left_insertion([1.0, 2.0, 3.0], 1.0), 0)
        self.assertEqual(left_insertion([1.0, 2.0, 3.0], 2.0), 1)
        self.assertEqual(left_insertion([1.0, 2.0, 3.0], 3.0), 2)

    def test_non_numeric_inputs(self):
        self.assertRaises(TypeError, left_insertion, ['a', 'b', 'c'], 'd')
        self.assertRaises(TypeError, left_insertion, [1, 2, 3], 'd')
