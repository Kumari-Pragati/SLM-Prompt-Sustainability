import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(add_str((), 'test'), [])

    def test_single_input(self):
        self.assertListEqual(add_str(('test',), 'test'), ['test', 'test'])

    def test_multiple_inputs(self):
        self.assertListEqual(add_str(((1, 'a'), (2, 'b')), 'test'), [1, 'a', 2, 'b', 'test'])

    def test_input_with_duplicates(self):
        self.assertListEqual(add_str(((1, 'a'), (1, 'a')), 'test'), [1, 'a', 1, 'a', 'test'])

    def test_input_with_empty_tuple(self):
        self.assertListEqual(add_str(((1, 'a'),()), 'test'), [1, 'a', 'test'])

    def test_input_with_string(self):
        self.assertListEqual(add_str(('test',), 'test2'), ['test', 'test', 'test2'])

    def test_input_with_different_types(self):
        with self.assertRaises(TypeError):
            add_str(((1, 'a'), (2, 3)), 'test')
