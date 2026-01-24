import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(odd_Days(2016), 1)
        self.assertEqual(odd_Days(2000), 3)
        self.assertEqual(odd_Days(1900), 6)

    def test_edge_input(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(365), 6)
        self.assertEqual(odd_Days(366), 0)
        self.assertEqual(odd_Days(7), 0)
        self.assertEqual(odd_Days(8), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, odd_Days, 'string')
        self.assertRaises(TypeError, odd_Days, -1)
        self.assertRaises(TypeError, odd_Days, float('nan'))
