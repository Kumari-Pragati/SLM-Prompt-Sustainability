import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_multiple_spaces('hello there'), 'hello there')
        self.assertEqual(remove_multiple_spaces('hello   there'), 'hello there')
        self.assertEqual(remove_multiple_spaces('  hello   there  '), 'hello there')

    def test_edge_cases(self):
        self.assertEqual(remove_multiple_spaces(''), '')
        self.assertEqual(remove_multiple_spaces('hello\nthere'), 'hello\nthere')
        self.assertEqual(remove_multiple_spaces('hello\tthere'), 'hello\tthere')
        self.assertEqual(remove_multiple_spaces('hello\rthere'), 'hello\rthere')
        self.assertEqual(remove_multiple_spaces('hello\x0bthere'), 'hello\x0bthere')

    def test_boundary_cases(self):
        self.assertEqual(remove_multiple_spaces('a '), 'a ')
        self.assertEqual(remove_multiple_spaces(' a '), 'a ')
        self.assertEqual(remove_multiple_spaces(' a '), 'a ')
        self.assertEqual(remove_multiple_spaces(' a '), 'a ')
        self.assertEqual(remove_multiple_spaces(' a '), 'a ')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_multiple_spaces, 123)
        self.assertRaises(TypeError, remove_multiple_spaces, None)
