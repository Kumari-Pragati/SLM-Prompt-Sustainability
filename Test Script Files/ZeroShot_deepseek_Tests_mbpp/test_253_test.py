import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_count_integer_with_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_count_integer_with_floats(self):
        self.assertEqual(count_integer([1.0, 2.0, 3.0, 4.0, 5.0]), 0)

    def test_count_integer_with_mixed_types(self):
        self.assertEqual(count_integer([1, '2', 3.0, 4, None]), 2)

    def test_count_integer_with_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_count_integer_with_none_in_list(self):
        self.assertEqual(count_integer([None]), 0)
