import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(octal_To_Decimal(10), 8)
        self.assertEqual(octal_To_Decimal(20), 24)
        self.assertEqual(octal_To_Decimal(30), 36)
        self.assertEqual(octal_To_Decimal(40), 48)
        self.assertEqual(octal_To_Decimal(50), 56)
        self.assertEqual(octal_To_Decimal(60), 64)
        self.assertEqual(octal_To_Decimal(70), 72)
        self.assertEqual(octal_To_Decimal(77), 77)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(octal_To_Decimal(0), 0)
        self.assertEqual(octal_To_Decimal(1), 1)
        self.assertEqual(octal_To_Decimal(2), 2)
        self.assertEqual(octal_To_Decimal(7), 7)
        self.assertEqual(octal_To_Decimal(87), 87)
        self.assertEqual(octal_To_Decimal(100), 100)
        self.assertEqual(octal_To_Decimal(177), 177)
        self.assertEqual(octal_To_Decimal(200), 200)
        self.assertEqual(octal_To_Decimal(377), 377)
        self.assertEqual(octal_To_Decimal(777), 777)

    def test_complex_inputs(self):
        self.assertEqual(octal_To_Decimal(101), 65)
        self.assertEqual(octal_To_Decimal(111), 73)
        self.assertEqual(octal_To_Decimal(121), 81)
        self.assertEqual(octal_To_Decimal(131), 91)
        self.assertEqual(octal_To_Decimal(141), 105)
        self.assertEqual(octal_To_Decimal(151), 119)
        self.assertEqual(octal_To_Decimal(161), 133)
        self.assertEqual(octal_To_Decimal(171), 147)
        self.assertEqual(octal_To_Decimal(201), 129)
        self.assertEqual(octal_To_Decimal(211), 145)
        self.assertEqual(octal_To_Decimal(221), 161)
        self.assertEqual(octal_To_Decimal(231), 177)
        self.assertEqual(octal_To_Decimal(241), 193)
        self.assertEqual(octal_To_Decimal(251), 209)
        self.assertEqual(octal_To_Decimal(261), 225)
        self.assertEqual(octal_To_Decimal(271), 241)
