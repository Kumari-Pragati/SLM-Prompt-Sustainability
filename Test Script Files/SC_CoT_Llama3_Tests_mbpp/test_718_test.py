import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_input(self):
        self.assertEqual(alternate_elements([]), [])

    def test_single_element_input(self):
        self.assertEqual(alternate_elements([1]), [])

    def test_even_length_input(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4]), [1, 3])

    def test_odd_length_input(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            alternate_elements('string')

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            alternate_elements(['a', 'b', 'c', 'd'])
