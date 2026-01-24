import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_empty_set(self):
        self.assertIsInstance(set_to_tuple({}), tuple)
        self.assertEqual(set_to_tuple({}), ())

    def test_single_element_set(self):
        for element in [1, 'a', 3.14]:
            self.assertIsInstance(set_to_tuple({element}), tuple)
            self.assertEqual(set_to_tuple({element}), (element,))

    def test_multiple_elements_set(self):
        for elements in [(1, 2, 3), ('a', 'b', 'c'), (3.14, 2.71, 1.41)]:
            self.assertIsInstance(set_to_tuple(set(elements)), tuple)
            sorted_elements = sorted(elements)
            self.assertEqual(set_to_tuple(set(elements)), tuple(sorted_elements))

    def test_duplicate_elements(self):
        for elements in [(1, 1, 2), ('a', 'a', 'b'), (3.14, 3.14, 2.71)]:
            self.assertIsInstance(set_to_tuple(set(elements)), tuple)
            sorted_elements = sorted(elements)
            self.assertEqual(set_to_tuple(set(elements)), tuple(sorted_elements))

    def test_empty_string_set(self):
        self.assertIsInstance(set_to_tuple({}), tuple)
        self.assertEqual(set_to_tuple({}), ())

    def test_string_set_with_whitespace(self):
        for string in ['  a  ', ' b   c  ', ' 1 2 3 ']:
            self.assertIsInstance(set_to_tuple(set(string.split())), tuple)
            self.assertEqual(set_to_tuple(set(string.split())), tuple(sorted(string.split())))

    def test_negative_numbers(self):
        for numbers in [(-1, 0, 1), (-1, -2, -3)]:
            self.assertIsInstance(set_to_tuple(set(numbers)), tuple)
            sorted_numbers = sorted(numbers)
            self.assertEqual(set_to_tuple(set(numbers)), tuple(sorted_numbers))

    def test_large_numbers(self):
        for numbers in [(1000000000000000000, 1, 2), (1000000000000000000, 1000000000000000000, 1000000000000000001)]:
            self.assertIsInstance(set_to_tuple(set(numbers)), tuple)
            sorted_numbers = sorted(numbers)
            self.assertEqual(set_to_tuple(set(numbers)), tuple(sorted_numbers))

    def test_float_numbers(self):
        for numbers in [(1.0, 2.0, 3.0), (1.0, 2.0, 3.1), (1.0, 2.0, 3.0000000001)]:
            self.assertIsInstance(set_to_tuple(set(numbers)), tuple)
            sorted_numbers = sorted(numbers)
            self.assertEqual(set_to_tuple(set(numbers)), tuple(sorted_numbers))

    def test_mixed_types(self):
        for elements in [(1, 'a', 3.14), (1, 'a', 3.14, None)]:
            with self.assertRaises(TypeError):
                set_to_tuple(set(elements))
