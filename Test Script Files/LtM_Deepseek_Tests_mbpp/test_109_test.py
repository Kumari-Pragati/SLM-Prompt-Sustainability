import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(odd_Equivalent('1011', 4), 3)
        self.assertEqual(odd_Equivalent('1111', 4), 4)
        self.assertEqual(odd_Equivalent('0000', 4), 0)

    def test_edge_conditions(self):
        self.assertEqual(odd_Equivalent('', 0), 0)
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(odd_Equivalent('1'*10000, 10000), 5000)
        self.assertEqual(odd_Equivalent('0'*10000, 10000), 0)

    def test_complex_cases(self):
        self.assertEqual(odd_Equivalent('1010101010', 10), 5)
        self.assertEqual(odd_Equivalent('0101010101', 10), 5)
        self.assertEqual(odd_Equivalent('1100110011', 10), 6)
