import unittest
from mbpp_206_code import Tuple

from 206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(concatenate_elements(()), tuple)
        self.assertIsInstance(concatenate_elements(()), tuple)
        self.assertIsInstance(concatenate_elements([]), tuple)
        self.assertIsInstance(concatenate_elements(list()), tuple)
        self.assertIsInstance(concatenate_elements(set()), tuple)
        self.assertIsInstance(concatenate_elements(range(0)), tuple)

    def test_single_element_tuple(self):
        self.assertIsInstance(concatenate_elements((1,)), tuple)
        self.assertIsInstance(concatenate_elements((1,)), tuple)
        self.assertEqual(concatenate_elements((1,)), (1,))

    def test_two_element_tuple(self):
        self.assertIsInstance(concatenate_elements((1, 2)), tuple)
        self.assertEqual(concatenate_elements((1, 2)), (1 + 2, 2))

    def test_three_element_tuple(self):
        self.assertIsInstance(concatenate_elements((1, 2, 3)), tuple)
        self.assertEqual(concatenate_elements((1, 2, 3)), (1 + 2, 2 + 3))

    def test_four_element_tuple(self):
        self.assertIsInstance(concatenate_elements((1, 2, 3, 4)), tuple)
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), (1 + 2, 2 + 3, 3 + 4))

    def test_negative_numbers(self):
        self.assertIsInstance(concatenate_elements((-1, 2, 3)), tuple)
        self.assertEqual(concatenate_elements((-1, 2, 3)), (-1 + 2, 2 + 3))

    def test_mixed_types(self):
        self.assertRaises(TypeError, concatenate_elements, (1, "2", 3))
        self.assertRaises(TypeError, concatenate_elements, (1, 2, "3"))
        self.assertRaises(TypeError, concatenate_elements, (1, 2, 3, "4"))
