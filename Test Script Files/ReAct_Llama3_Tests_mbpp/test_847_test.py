import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_list(self):
        self.assertEqual(lcopy([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(lcopy([-1, -2, -3]), [-1, -2, -3])

    def test_list_with_mixed_types(self):
        self.assertEqual(lcopy([1, 'a', 3.14]), [1, 'a', 3.14])

    def test_list_with_duplicates(self):
        self.assertEqual(lcopy([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])

    def test_list_with_empty_string(self):
        self.assertEqual(lcopy(['a', '', 'c']), ['a', '', 'c'])

    def test_list_with_none(self):
        self.assertEqual(lcopy([1, None, 3]), [1, None, 3])
