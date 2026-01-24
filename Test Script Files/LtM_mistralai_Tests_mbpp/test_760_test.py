import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_multiple_elements(self):
        self.assertEqual(unique_Element([1, 2], 2), 'NO')

    def test_duplicate_elements(self):
        self.assertEqual(unique_Element([1, 1], 2), 'NO')

    def test_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_negative_numbers(self):
        self.assertEqual(unique_Element([-1, -2], 2), 'NO')

    def test_zero(self):
        self.assertEqual(unique_Element([0], 1), 'YES')

    def test_large_numbers(self):
        self.assertEqual(unique_Element([1000000, 2000000], 2), 'NO')
