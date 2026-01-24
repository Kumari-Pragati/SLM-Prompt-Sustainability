import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(empty_list(3), [{}, {}, {}])

    def test_edge_cases(self):
        self.assertEqual(empty_list(0), [])
        self.assertEqual(empty_list(1), [{}])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            empty_list(-1)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            empty_list(3.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            empty_list('abc')
