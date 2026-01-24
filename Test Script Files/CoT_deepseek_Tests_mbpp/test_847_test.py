import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_list(self):
        self.assertEqual(lcopy([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(lcopy([1, 2, 2]), [1, 2, 2])

    def test_large_list(self):
        self.assertEqual(lcopy(list(range(1, 1001))), list(range(1, 1001)))

    def test_negative_numbers(self):
        self.assertEqual(lcopy([-1, -2, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(lcopy([-1, 0, 1]), [-1, 0, 1])

    def test_non_integer_elements(self):
        self.assertEqual(lcopy([1.1, 2.2, 3.3]), [1.1, 2.2, 3.3])

    def test_nested_list(self):
        self.assertEqual(lcopy([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_string_elements(self):
        self.assertEqual(lcopy(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_none_elements(self):
        self.assertEqual(lcopy([None, None]), [None, None])
