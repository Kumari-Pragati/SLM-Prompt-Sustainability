import unittest
from mbpp_172_code import count_occurance

class TestCountOcurance(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("stds"), 2)
        self.assertEqual(count_occurance("stdstd"), 3)

    def test_edge(self):
        self.assertEqual(count_occurance(""), 0)
        self.assertEqual(count_occurance("stds"), 1)
        self.assertEqual(count_occurance("stdstds"), 2)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            count_occurance(123)
        with self.assertRaises(TypeError):
            count_occurance([1, 2, 3])

    def test_empty_string(self):
        self.assertEqual(count_occurance(""), 0)

    def test_no_match(self):
        self.assertEqual(count_occurance("hello"), 0)
        self.assertEqual(count_occurance("world"), 0)
