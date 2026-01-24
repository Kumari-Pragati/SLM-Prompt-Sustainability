import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_non_integer_values(self):
        self.assertEqual(count_integer([1, 2, 'a', 4, 5]), 3)

    def test_all_non_integer_values(self):
        self.assertEqual(count_integer(['a', 'b', 'c', 'd', 'e']), 0)

    def test_mixed_integer_and_non_integer_values(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3]), 3)

    def test_single_integer_value(self):
        self.assertEqual(count_integer([1]), 1)

    def test_multiple_integer_values(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_large_list_of_integer_values(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_large_list_of_non_integer_values(self):
        self.assertEqual(count_integer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), 0)

    def test_list_with_mixed_integer_and_non_integer_values(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']), 5)
