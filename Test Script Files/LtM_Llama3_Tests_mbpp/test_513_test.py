import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(add_str([1, 2], 3), [1, 2, 3])

    def test_empty_input(self):
        self.assertEqual(add_str([], 4), [])

    def test_single_element_input(self):
        self.assertEqual(add_str([1], 2), [1, 2])

    def test_empty_K(self):
        self.assertEqual(add_str([1, 2], ''), [])

    def test_non_integer_K(self):
        self.assertEqual(add_str([1, 2], '3'), [1, 2, '3'])

    def test_multiple_elements_input(self):
        self.assertEqual(add_str([1, 2, 3], 4), [1, 2, 3, 4])

    def test_empty_input_and_K(self):
        self.assertEqual(add_str([], ''), [])
