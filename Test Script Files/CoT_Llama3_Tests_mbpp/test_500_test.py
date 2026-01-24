import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(concatenate_elements(['apple', 'banana', 'cherry']),'apple banana cherry')

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]),'')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['hello']),'hello')

    def test_multiple_spaces(self):
        self.assertEqual(concatenate_elements(['hello', 'world']),'hello world')

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate_elements([1, 2, 3])

    def test_mixed_type_elements(self):
        with self.assertRaises(TypeError):
            concatenate_elements([1, 'hello', 3.14])
