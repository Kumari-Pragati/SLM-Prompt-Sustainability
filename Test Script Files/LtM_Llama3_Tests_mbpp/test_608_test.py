import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 3)
        self.assertEqual(bell_Number(4), 5)
        self.assertEqual(bell_Number(5), 8)

    def test_edge(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(-1), None)

    def test_large(self):
        self.assertEqual(bell_Number(10), 55)
        self.assertEqual(bell_Number(20), 676)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            bell_Number('a')
