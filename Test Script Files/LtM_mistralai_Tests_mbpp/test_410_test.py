import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_simple_int_list(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_all_floats(self):
        self.assertIsNone(min_val([1.1, 2.2, 3.3]))

    def test_all_strings(self):
        self.assertIsNone(min_val(["a", "b", "c"]))

    def test_mixed_types(self):
        self.assertIsNone(min_val([1, "a", 2.5]))

    def test_min_int_value(self):
        self.assertEqual(min_val([-100, -5, 0, 5, 100]), -100)

    def test_max_int_value(self):
        self.assertEqual(min_val([2147483647, 2147483646, 0, -1, -2147483648]), -2147483648)
