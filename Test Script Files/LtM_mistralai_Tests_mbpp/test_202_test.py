import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_even('abcde'), 'acde')
        self.assertEqual(remove_even('ABCDE'), 'ACDE')
        self.assertEqual(remove_even('12345'), '135')

    def test_edge_and_boundary(self):
        self.assertEqual(remove_even(''), '')
        self.assertEqual(remove_even('a'), 'a')
        self.assertEqual(remove_even('abc'), 'ac')
        self.assertEqual(remove_even('abcdefg'), 'acdefg')
        self.assertEqual(remove_even('abcdefghijklmnopqrstuvwxyz'), 'acdefghijklmnopqrstuvwxyz')
        self.assertEqual(remove_even('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'ACDEFGHIJKLMNOPQRSTUVWXYZ')
        self.assertEqual(remove_even('1234567890'), '135789')
        self.assertEqual(remove_even('12345678901234567890'), '135789123456789')

    def test_complex_input(self):
        self.assertEqual(remove_even('a1b2c3'), '1c3')
        self.assertEqual(remove_even('a1b2c3d4'), '1c3d4')
        self.assertEqual(remove_even('a1b2c3d4e5'), '1c3d4e5')
        self.assertEqual(remove_even('a1b2c3d4e5f6'), '1c3d4e5f6')
        self.assertEqual(remove_even('a1b2c3d4e5f6g7'), '1c3d4e5f6g7')
