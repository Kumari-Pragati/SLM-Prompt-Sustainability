import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_length('101010', 10), 2)
        self.assertEqual(find_length('111111', 6), 6)
        self.assertEqual(find_length('000000', 6), 0)
        self.assertEqual(find_length('101010', 5), 1)
        self.assertEqual(find_length('111111', 3), 3)

    def test_edge_cases(self):
        self.assertEqual(find_length('111111', 1), 1)
        self.assertEqual(find_length('000000', 1), 0)
        self.assertEqual(find_length('101010', 0), 0)

    def test_special_cases(self):
        self.assertEqual(find_length('101010', 11), 2)
        self.assertEqual(find_length('111111', 7), 6)
        self.assertEqual(find_length('000000', 7), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_length(None, 5)
        with self.assertRaises(TypeError):
            find_length('101010', None)
        with self.assertRaises(TypeError):
            find_length('', 5)
