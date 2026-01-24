import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(add_str([1, 2], 'K'), [1, 2, 'K'])

    def test_edge(self):
        self.assertEqual(add_str([], 'K'), ['K'])
        self.assertEqual(add_str(['A'], 'K'), ['A', 'K'])

    def test_edge2(self):
        self.assertEqual(add_str([1, 2, 3], 'K'), [1, 2, 3, 'K'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_str(None, 'K')

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            add_str([1, 2], None)
