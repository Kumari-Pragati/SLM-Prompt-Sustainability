import unittest
from mbpp_204_code import count

class TestCount(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count('hello', 'l'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count('', 'a'), 0)

    def test_boundary_case_single_character(self):
        self.assertEqual(count('a', 'a'), 1)
        self.assertEqual(count('a', 'b'), 0)

    def test_boundary_case_repeated_character(self):
        self.assertEqual(count('aaaa', 'a'), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count(123, 'a')
        with self.assertRaises(TypeError):
            count('hello', 123)
