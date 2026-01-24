import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)
        self.assertEqual(odd_Equivalent('10101', 5), 3)

    def test_edge_input(self):
        self.assertEqual(odd_Equivalent('', 0), 0)
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('111111', 6), 6)

    def test_boundary_input(self):
        self.assertEqual(odd_Equivalent('10101010101010101010101', 20), 10)
        self.assertEqual(odd_Equivalent('01010101010101010101010', 20), 10)
