import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_duplicates(self):
        self.assertEqual(unique_Element([1, 1, 2], 3), 'NO')

    def test_all_unique(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'YES')

    def test_negative_numbers(self):
        self.assertEqual(unique_Element([-1, -2, -3], 3), 'YES')

    def test_mixed_numbers(self):
        self.assertEqual(unique_Element([1, -2, 3], 3), 'YES')

    def test_no_elements(self):
        with self.assertRaises(TypeError):
            unique_Element(None, 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            unique_Element([1], -1)
