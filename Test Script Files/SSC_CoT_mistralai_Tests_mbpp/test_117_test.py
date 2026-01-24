import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(list_to_float([(1, 2.5), ('a', 3.14), ('b', 0)]), "([('a', 3.14)], [('b', 0)]")

    def test_empty_input(self):
        self.assertEqual(list_to_float([]), "[]")

    def test_single_input(self):
        self.assertEqual(list_to_float([(1)]), "[]")
        self.assertEqual(list_to_float([('a')]), "[]")

    def test_all_strings(self):
        self.assertEqual(list_to_float([('a'), ('b'), ('c')]), "[]")

    def test_all_floats(self):
        self.assertEqual(list_to_float([(1.1, 2.2), (3.3, 4.4)]), "([], [(3.3, 4.4)])")

    def test_mixed_input(self):
        self.assertEqual(list_to_float([(1, 'str'), ('float', 3.14), ('another_str', 0)]), "([('str', 3.14)], [('another_str', 0)]")

    def test_invalid_input(self):
        self.assertRaises(TypeError, list_to_float, [(1, 'not_a_number')])
