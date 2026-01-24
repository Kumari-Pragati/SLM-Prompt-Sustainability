import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_simple_integer_list(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_list_with_only_non_integer(self):
        self.assertEqual(count_integer(['a', 'b', 'c']), 0)

    def test_list_with_mixed_types(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3]), 3)

    def test_min_integer(self):
        self.assertEqual(count_integer([-9223372036854775808]), 1)

    def test_max_integer(self):
        self.assertEqual(count_integer([9223372036854775807]), 1)
