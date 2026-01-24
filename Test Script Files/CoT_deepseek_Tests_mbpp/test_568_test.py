import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(empty_list(5), [{}]*5)

    def test_zero_length(self):
        self.assertEqual(empty_list(0), [])

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            empty_list(-5)

    def test_large_length(self):
        self.assertEqual(len(empty_list(1000)), 1000)

    def test_non_integer_length(self):
        with self.assertRaises(TypeError):
            empty_list(5.5)
