import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(odd_Equivalent('10101', 5), 3)
        self.assertEqual(odd_Equivalent('11111', 5), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('11', 2), 2)
        self.assertEqual(odd_Equivalent('111', 3), 3)
        self.assertEqual(odd_Equivalent('1111', 4), 3)
        self.assertEqual(odd_Equivalent('11111', 6), 5)

    def test_special_cases(self):
        self.assertEqual(odd_Equivalent('00101', 5), 1)
        self.assertEqual(odd_Equivalent('10010', 5), 1)
        self.assertEqual(odd_Equivalent('10100', 5), 2)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, odd_Equivalent, '101', -1)
        self.assertRaises(ValueError, odd_Equivalent, '10101', 0)
        self.assertRaises(ValueError, odd_Equivalent, '', 10)
        self.assertRaises(ValueError, odd_Equivalent, None, 10)
        self.assertRaises(ValueError, odd_Equivalent, 10, 10)
