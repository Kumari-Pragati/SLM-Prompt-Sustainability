import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_X((1, 2, 'X', 4, 'X'), 'X'), 2)

    def test_single_element_tuple(self):
        self.assertEqual(count_X(('X',), 'X'), 1)
        self.assertEqual(count_X(('X',), 'Y'), 0)

    def test_empty_tuple(self):
        self.assertEqual(count_X((), 'X'), 0)

    def test_case_insensitivity(self):
        self.assertEqual(count_X(('x', 'X'), 'X'), 2)

    def test_non_string_elements(self):
        self.assertEqual(count_X((1, 'X', 3.5), 'X'), 1)

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            count_X('X', 'X')
