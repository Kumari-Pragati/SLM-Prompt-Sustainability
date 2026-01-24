import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_charac("Hello"), 5)
        self.assertEqual(count_charac("World"), 5)
        self.assertEqual(count_charac("Python"), 6)

    def test_edge_cases(self):
        self.assertEqual(count_charac(""), 0)
        self.assertEqual(count_charac("a"), 1)
        self.assertEqual(count_charac("abc"), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_charac(123)
        with self.assertRaises(TypeError):
            count_charac([1, 2, 3])

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            count_charac(None)
        with self.assertRaises(TypeError):
            count_charac(True)
