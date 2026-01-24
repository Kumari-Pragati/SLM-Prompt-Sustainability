import unittest
from mbpp_194_code import octal_To_Decimal

class TestOctalToDecimal(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(octal_To_Decimal('10'), 8)
        self.assertEqual(octal_To_Decimal('123'), 83)
        self.assertEqual(octal_To_Decimal('777'), 511)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(octal_To_Decimal('0'), 0)
        self.assertEqual(octal_To_Decimal('7777777'), 4095)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(octal_To_Decimal('10000000'), 4096)
        self.assertEqual(octal_To_Decimal('77777777'), 4095)
