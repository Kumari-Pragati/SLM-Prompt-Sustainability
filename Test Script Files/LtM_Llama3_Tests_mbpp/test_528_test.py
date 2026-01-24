import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_length([1, 2, 3]), (1, 1))
        self.assertEqual(min_length(['a', 'b', 'c']), (1, 'a'))
        self.assertEqual(min_length([5, 5, 5]), (5, 5))

    def test_empty(self):
        self.assertEqual(min_length([]), (0, None))

    def test_single_element(self):
        self.assertEqual(min_length(['hello']), (5, 'hello'))

    def test_all_equal(self):
        self.assertEqual(min_length([1, 1, 1]), (1, 1))

    def test_mixed_types(self):
        self.assertEqual(min_length([1, 'a', 3.14]), (1, 1))

    def test_longest_string(self):
        self.assertEqual(min_length(['hello', 'world']), (5, 'hello'))

    def test_longest_number(self):
        self.assertEqual(min_length([100, 200, 300]), (3, 100))
