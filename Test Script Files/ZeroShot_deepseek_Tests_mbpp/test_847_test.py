import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):

    def test_lcopy_with_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_lcopy_with_single_element_list(self):
        self.assertEqual(lcopy([1]), [1])

    def test_lcopy_with_multiple_element_list(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_lcopy_with_duplicate_elements(self):
        self.assertEqual(lcopy([1, 1, 2, 2]), [1, 1, 2, 2])

    def test_lcopy_with_negative_numbers(self):
        self.assertEqual(lcopy([-1, -2, -3]), [-1, -2, -3])

    def test_lcopy_with_mixed_numbers(self):
        self.assertEqual(lcopy([-1, 0, 1]), [-1, 0, 1])

    def test_lcopy_with_non_integer_elements(self):
        self.assertEqual(lcopy([1.1, 2.2, 3.3]), [1.1, 2.2, 3.3])

    def test_lcopy_with_non_integer_mixed_list(self):
        self.assertEqual(lcopy([1, 2.2, '3']), [1, 2.2, '3'])

    def test_lcopy_with_string_elements(self):
        self.assertEqual(lcopy(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_lcopy_with_string_mixed_list(self):
        self.assertEqual(lcopy([1, 'b', 'c']), [1, 'b', 'c'])
