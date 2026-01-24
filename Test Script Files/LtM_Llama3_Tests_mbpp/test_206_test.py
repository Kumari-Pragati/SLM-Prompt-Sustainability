import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_single_element_input(self):
        self.assertEqual(concatenate_elements((1,)), (1,))

    def test_two_elements_input(self):
        self.assertEqual(concatenate_elements((1, 2)), (3,))

    def test_three_elements_input(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (4, 5))

    def test_long_input(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5, 6)), (7, 8, 9))

    def test_negative_numbers_input(self):
        self.assertEqual(concatenate_elements((-1, -2)), (-3,))

    def test_mixed_numbers_input(self):
        self.assertEqual(concatenate_elements((1, -2, 3)), (1, 1))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements(("a", "b"))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements([1, 2])
