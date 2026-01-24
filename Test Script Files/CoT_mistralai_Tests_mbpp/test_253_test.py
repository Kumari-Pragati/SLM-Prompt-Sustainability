import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_list_with_ints(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_list_with_mixed_types(self):
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3]), 3)

    def test_list_with_only_non_ints(self):
        self.assertEqual(count_integer(['a', 'b', 'c']), 0)

    def test_list_with_floats(self):
        self.assertEqual(count_integer([1.0, 2.0, 3.0]), 3)

    def test_list_with_complex_numbers(self):
        self.assertEqual(count_integer([1j, 2j, 3j]), 0)

    def test_list_with_empty_elements(self):
        self.assertEqual(count_integer([1, None, 2, None, 3]), 3)
