import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_integer([1, 2, 3, 'a', 'b', 'c', 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_list_with_only_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_list_with_only_non_integers(self):
        self.assertEqual(count_integer(['a', 'b', 'c', 'd', 'e']), 0)

    def test_list_with_mixed_integers_and_non_integers(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3, 'c']), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(count_integer([1, 1, 2, 2, 3, 3]), 3)

    def test_list_with_negative_integers(self):
        self.assertEqual(count_integer([-1, -2, -3, -4, -5]), 5)

    def test_list_with_zero(self):
        self.assertEqual(count_integer([0]), 1)
