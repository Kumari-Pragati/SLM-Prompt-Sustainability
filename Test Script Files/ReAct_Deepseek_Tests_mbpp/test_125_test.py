import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_length('01010101', 8), 4)
        self.assertEqual(find_length('11111111', 8), 0)
        self.assertEqual(find_length('00000000', 8), 0)
        self.assertEqual(find_length('10101010', 8), 4)

    def test_edge_cases(self):
        self.assertEqual(find_length('', 0), 0)
        self.assertEqual(find_length('0', 1), 1)
        self.assertEqual(find_length('1', 1), 0)
        self.assertEqual(find_length('0000000000000000000000000000000000000000000000000000000000000000', 100), 100)
        self.assertEqual(find_length('1111111111111111111111111111111111111111111111111111111111111111', 100), 0)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            find_length(123456, 8)
        with self.assertRaises(TypeError):
            find_length('01010101', '8')
        with self.assertRaises(ValueError):
            find_length('01010101', -1)
