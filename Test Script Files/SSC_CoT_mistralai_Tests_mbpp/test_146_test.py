import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(ascii_value_string("abc"), (97, 98, 99))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(ascii_value_string(""), ())
        self.assertEqual(ascii_value_string("a" * 10000), (97,) * 10000)
        self.assertEqual(ascii_value_string("z"), 122)
        self.assertEqual(ascii_value_string("A"), 65)
        self.assertEqual(ascii_value_string("0"), 48)
        self.assertEqual(ascii_value_string("!"), 33)

    def test_special_or_corner_cases(self):
        self.assertEqual(ascii_value_string("ABCabc123!@#"), (65, 66, 67, 97, 98, 99, 49, 50, 33, 64))
        self.assertEqual(ascii_value_string(""), ())
        self.assertEqual(ascii_value_string(" "), (32,))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, ascii_value_string, 123)
        self.assertRaises(TypeError, ascii_value_string, [])
        self.assertRaises(TypeError, ascii_value_string, (1, 2, 3))
        self.assertRaises(TypeError, ascii_value_string, None)
