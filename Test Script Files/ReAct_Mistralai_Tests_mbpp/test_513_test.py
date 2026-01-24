import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(add_str((), 'test'), [])

    def test_single_input(self):
        self.assertListEqual(add_str(('test',), 'K'), ['test', 'K'])

    def test_multiple_inputs(self):
        self.assertListEqual(add_str(((1, 'a'), (2, 'b')), 'K'), [1, 'a', 2, 'b', 'K'])

    def test_input_with_duplicates(self):
        self.assertListEqual(add_str(((1, 'a'), (1, 'a')), 'K'), [1, 'a', 1, 'a', 'K'])

    def test_input_with_empty_tuple(self):
        self.assertListEqual(add_str(((1, 'a'),), 'K'), [1, 'a', 'K'])

    def test_input_with_only_K(self):
        self.assertListEqual(add_str(((),), 'K'), ['K'])

    def test_input_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            add_str(((1, 2),), 'K')
