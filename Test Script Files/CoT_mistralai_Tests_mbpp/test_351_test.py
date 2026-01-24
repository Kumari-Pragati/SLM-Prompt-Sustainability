import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_single_element(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_repeated_elements(self):
        self.assertEqual(first_Element([1, 1, 2, 2, 3, 3, 4, 4, 5], 5, 2), 1)

    def test_k_greater_than_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 4), -1)

    def test_k_less_than_1(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 0), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, first_Element, [1, 2, 3], 'a', 1)
        self.assertRaises(TypeError, first_Element, [1, 2, 3], 3, 'a')
