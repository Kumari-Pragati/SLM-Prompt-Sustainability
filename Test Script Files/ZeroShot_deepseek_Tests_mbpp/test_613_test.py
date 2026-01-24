import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_value([]), [])

    def test_single_list(self):
        self.assertEqual(maximum_value([('a', [1, 2, 3])]), [('a', 3)])

    def test_multiple_lists(self):
        self.assertEqual(maximum_value([('a', [1, 2, 3]), ('b', [4, 5, 6])]), [('a', 3), ('b', 6)])

    def test_negative_numbers(self):
        self.assertEqual(maximum_value([('a', [-1, -2, -3])]), [('a', -1)])

    def test_mixed_numbers(self):
        self.assertEqual(maximum_value([('a', [1, -2, 3])]), [('a', 3)])
