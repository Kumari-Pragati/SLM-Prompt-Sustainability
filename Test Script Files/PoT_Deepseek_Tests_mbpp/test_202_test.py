import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(remove_even('abcdefg'), 'bdf')
        self.assertEqual(remove_even('1234567890'), '24680')
        self.assertEqual(remove_even('!@#$%^&*()'), '#%&()')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(remove_even(''), '')
        self.assertEqual(remove_even('a'), '')
        self.assertEqual(remove_even('1'), '')
        self.assertEqual(remove_even('!'), '')

    def test_corner_cases(self):
        self.assertEqual(remove_even('abcdefghijklmnopqrstuvwxyz'), 'bdfhjlnprtvxz')
        self.assertEqual(remove_even('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'BDFHJLNPRTVXZ')
        self.assertEqual(remove_even('0123456789'), '2468')
