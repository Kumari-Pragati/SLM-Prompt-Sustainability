import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalence(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)
        self.assertEqual(odd_Equivalent('101', 3), 1)
        self.assertEqual(odd_Equivalent('110', 3), 1)
        self.assertEqual(odd_Equivalent('000', 3), 0)

    def test_edge_cases(self):
        self.assertEqual(odd_Equivalent('', 3), 0)
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('1', 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Equivalent(None, 3)
        with self.assertRaises(TypeError):
            odd_Equivalent('abc', None)
        with self.assertRaises(TypeError):
            odd_Equivalent('abc', 'xyz')
