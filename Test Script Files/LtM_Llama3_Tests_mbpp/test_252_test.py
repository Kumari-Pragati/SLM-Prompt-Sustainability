import unittest
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(convert([1, 2, 3]), ([1, 2, 3]))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            convert([])

    def test_single_element(self):
        self.assertEqual(convert([1]), ([1]))

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, 2, 3]), ([-1, 2, 3]))

    def test_complex_numbers(self):
        self.assertEqual(convert([1 + 2j, 3 - 4j]), ([1 + 2j, 3 - 4j]))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            convert([1, 'a', 3])
