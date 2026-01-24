import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_multiple_elements(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'NO')

    def test_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'NO')

    def test_duplicate_elements(self):
        self.assertEqual(unique_Element([1, 1, 2], 3), 'NO')

    def test_negative_number(self):
        self.assertRaises(ValueError, unique_Element, [-1], 1)

    def test_non_iterable_input(self):
        self.assertRaises(TypeError, unique_Element, 'string', 1)
