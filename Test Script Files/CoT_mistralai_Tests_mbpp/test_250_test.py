import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(count_X((), 'x'), 0)

    def test_single_element_tuple(self):
        self.assertEqual(count_X((1,), 'x'), 0)
        self.assertEqual(count_X(('x',), 'x'), 1)

    def test_multiple_elements_tuple(self):
        self.assertEqual(count_X((1, 2, 'x', 'y', 'x'), 'x'), 2)
        self.assertEqual(count_X((1, 2, 'y', 'x', 'z'), 'x'), 1)

    def test_mixed_types_tuple(self):
        self.assertEqual(count_X((1, 2.0, 'x', 3, 'y'), 'x'), 1)
        self.assertEqual(count_X((1, 2.0, 'x', 3, 'y'), 'Y'), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_X, 1, 'x')
        self.assertRaises(TypeError, count_X, ('x', 'y'), 1)
