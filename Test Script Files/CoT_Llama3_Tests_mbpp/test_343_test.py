import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(dig_let("hello123"), (4, 3))
        self.assertEqual(dig_let("abc456"), (3, 3))
        self.assertEqual(dig_let("hello world"), (11, 0))

    def test_edge_cases(self):
        self.assertEqual(dig_let(""), (0, 0))
        self.assertEqual(dig_let("123"), (0, 3))
        self.assertEqual(dig_let("abc"), (3, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            dig_let(123)
        with self.assertRaises(TypeError):
            dig_let([1, 2, 3])
