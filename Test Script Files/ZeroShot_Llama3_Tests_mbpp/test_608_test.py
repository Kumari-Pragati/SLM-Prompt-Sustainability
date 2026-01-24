import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_bell_number(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 3)
        self.assertEqual(bell_Number(4), 5)
        self.assertEqual(bell_Number(5), 8)
        self.assertEqual(bell_Number(6), 13)
        self.assertEqual(bell_Number(7), 21)
        self.assertEqual(bell_Number(8), 34)
        self.assertEqual(bell_Number(9), 55)
        self.assertEqual(bell_Number(10), 89)

    def test_bell_number_invalid_input(self):
        with self.assertRaises(TypeError):
            bell_Number(-1)
        with self.assertRaises(TypeError):
            bell_Number(None)
        with self.assertRaises(TypeError):
            bell_Number("a")
