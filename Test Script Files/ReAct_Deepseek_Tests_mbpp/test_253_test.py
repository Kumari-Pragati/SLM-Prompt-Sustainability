import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_integer([1, 2, 3, 'a', 'b', 4]), 3)

    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_all_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_all_non_integers(self):
        self.assertEqual(count_integer(['a', 'b', 'c', 'd']), 0)

    def test_mixed_integers_and_non_integers(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3]), 2)

    def test_single_integer(self):
        self.assertEqual(count_integer([5]), 1)

    def test_single_non_integer(self):
        self.assertEqual(count_integer(['hello']), 0)
