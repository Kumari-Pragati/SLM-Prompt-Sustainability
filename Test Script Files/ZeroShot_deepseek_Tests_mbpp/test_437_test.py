import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_remove_odd(self):
        self.assertEqual(remove_odd('1234567890'), '24680')
        self.assertEqual(remove_odd('abcdefghijklmnopqrstuvwxyz'), 'bdfhjlnprtvxz')
        self.assertEqual(remove_odd(''), '')
        self.assertEqual(remove_odd('a'), '')
        self.assertEqual(remove_odd('1'), '')
        self.assertEqual(remove_odd('0123456789'), '2468')
