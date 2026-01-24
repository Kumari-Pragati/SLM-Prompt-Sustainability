import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_count_integer_positive(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_count_integer_negative(self):
        self.assertEqual(count_integer([-1, -2, -3, -4, -5]), 5)

    def test_count_integer_mixed(self):
        self.assertEqual(count_integer([1, 2, 'a', 4, 5]), 3)

    def test_count_integer_empty(self):
        self.assertEqual(count_integer([]), 0)

    def test_count_integer_non_integer(self):
        self.assertEqual(count_integer([1, 2, 'a', 4, 'b']), 3)
