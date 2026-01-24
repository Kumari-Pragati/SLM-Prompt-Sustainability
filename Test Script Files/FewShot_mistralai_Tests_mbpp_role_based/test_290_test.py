import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(max_length([1, 'abc', 3.14]), (3, 'abc'))

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length([1]), (1, 1))

    def test_negative_list(self):
        self.assertEqual(max_length([-1, -2, -3]), (3, -1))

    def test_mixed_list(self):
        self.assertEqual(max_length([1, 'xyz', 2.0, 'abc']), (4, 'abc'))

    def test_list_with_none(self):
        self.assertEqual(max_length([None, 1, 'abc']), (3, 'abc'))
