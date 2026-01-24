import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5], 5), 'YES')

    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_empty_array(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_all_same_elements(self):
        self.assertEqual(unique_Element([1, 1, 1, 1, 1], 5), 'YES')

    def test_multiple_unique_elements(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5], 5), 'YES')

    def test_negative_numbers(self):
        self.assertEqual(unique_Element([-1, -2, -3, -4, -5], 5), 'YES')

    def test_mixed_numbers(self):
        self.assertEqual(unique_Element([1, -2, 3, -4, 5], 5), 'YES')

    def test_large_numbers(self):
        self.assertEqual(unique_Element([1000000, 2000000, 3000000, 4000000, 5000000], 5), 'YES')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            unique_Element("1, 2, 3, 4, 5", 5)

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            unique_Element([1, 2, 3, 4, 5], -5)
