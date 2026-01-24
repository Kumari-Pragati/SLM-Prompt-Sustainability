import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(maximum_value([("a", [1, 2, 3]), ("b", [4, 5, 6])]), [("a", 3), ("b", 6)])

    def test_empty_input(self):
        self.assertEqual(maximum_value([]), [])

    def test_single_element_list(self):
        self.assertEqual(maximum_value([("a", [1])]), [("a", 1)])

    def test_empty_list(self):
        self.assertEqual(maximum_value([("a", [])]), [("a",)])

    def test_max_value(self):
        self.assertEqual(maximum_value([("a", [1, 2, 3, 4, 5])]), [("a", 5)])

    def test_min_value(self):
        self.assertEqual(maximum_value([("a", [1, 2, 3, 4, 0])]), [("a", 4)])

    def test_multiple_lists(self):
        self.assertEqual(maximum_value([("a", [1, 2, 3]), ("b", [4, 5, 6]), ("c", [7, 8, 9])]), [("a", 3), ("b", 6), ("c", 9)])
