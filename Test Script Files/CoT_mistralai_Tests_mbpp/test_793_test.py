import unittest
from793_code import last

class TestLastFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(last([], 10, 0), -1)

    def test_single_element(self):
        self.assertEqual(last([10], 10, 0), 0)
        self.assertEqual(last([10], 5, 0), -1)

    def test_multiple_elements_found(self):
        self.assertEqual(last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 9) , 9)
        self.assertEqual(last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4) , 4)

    def test_multiple_elements_not_found(self):
        self.assertEqual(last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15, 9), -1)
        self.assertEqual(last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 0), -1)

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, last, 'string', 10, 0)
        self.assertRaises(TypeError, last, [1, 2, 3], 'int', 0)
        self.assertRaises(TypeError, last, [1, 2, 3], 10.5, 0)

    def test_invalid_input_index(self):
        self.assertRaises(IndexError, last, [1, 2, 3], 10, -1)
        self.assertRaises(IndexError, last, [1, 2, 3], 10, len([1, 2, 3]) + 1)
