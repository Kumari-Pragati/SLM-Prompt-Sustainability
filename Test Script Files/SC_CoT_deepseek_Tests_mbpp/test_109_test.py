import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('1011', 4), 3)

    def test_boundary_case(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('', 0), 0)

    def test_edge_case(self):
        self.assertEqual(odd_Equivalent('0000', 4), 0)
        self.assertEqual(odd_Equivalent('1111', 4), 4)
        self.assertEqual(odd_Equivalent('10101010', 8), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Equivalent(1011, '4')
        with self.assertRaises(TypeError):
            odd_Equivalent('1011', '4')
        with self.assertRaises(TypeError):
            odd_Equivalent(1011, 4)
        with self.assertRaises(ValueError):
            odd_Equivalent('1011', -4)
        with self.assertRaises(TypeError):
            odd_Equivalent('1011', 4.5)
