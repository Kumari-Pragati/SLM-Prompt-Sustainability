import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):
    def test_bell_number(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 5)
        self.assertEqual(bell_Number(4), 9)
        self.assertEqual(bell_Number(5), 14)
        self.assertEqual(bell_Number(6), 22)
        self.assertEqual(bell_Number(7), 37)
        self.assertEqual(bell_Number(8), 59)
        self.assertEqual(bell_Number(9), 92)
        self.assertEqual(bell_Number(10), 149)
        self.assertEqual(bell_Number(-1), None)
        self.assertEqual(bell_Number(0.5), None)
        self.assertEqual(bell_Number(None), None)
