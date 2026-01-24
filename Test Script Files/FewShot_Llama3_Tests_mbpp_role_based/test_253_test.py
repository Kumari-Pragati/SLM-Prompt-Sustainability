import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_list_of_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_list_of_mixed_types(self):
        self.assertEqual(count_integer([1, 'a', 3, 4, 5.5]), 3)

    def test_list_of_integers_with_duplicates(self):
        self.assertEqual(count_integer([1, 2, 2, 3, 3, 3]), 3)

    def test_list_of_integers_with_negative_numbers(self):
        self.assertEqual(count_integer([-1, 0, 1, 2, 3]), 3)
