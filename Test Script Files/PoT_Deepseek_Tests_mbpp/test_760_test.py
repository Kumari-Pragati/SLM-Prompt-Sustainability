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

    def test_mixed_elements(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5], 5), 'YES')

    def test_negative_numbers(self):
        self.assertEqual(unique_Element([-1, -2, -3, -4, -5], 5), 'YES')

    def test_mixed_negative_and_positive(self):
        self.assertEqual(unique_Element([-1, 2, -3, 4, -5], 5), 'YES')

    def test_large_numbers(self):
        self.assertEqual(unique_Element([1000000, 2000000, 3000000, 4000000, 5000000], 5), 'YES')

    def test_large_array(self):
        self.assertEqual(unique_Element(list(range(1, 1000001)), 1000000), 'YES')

    def test_duplicate_elements(self):
        self.assertEqual(unique_Element([1, 2, 2, 3, 4, 5], 6), 'NO')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            unique_Element("not a list", 1)
