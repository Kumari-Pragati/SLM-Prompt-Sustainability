import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_divisor(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(3), 2)
        self.assertEqual(divisor(4), 2)
        self.assertEqual(divisor(5), 2)
        self.assertEqual(divisor(6), 2)
        self.assertEqual(divisor(7), 1)
        self.assertEqual(divisor(8), 3)
        self.assertEqual(divisor(9), 3)
        self.assertEqual(divisor(10), 2)
        self.assertEqual(divisor(11), 1)
        self.assertEqual(divisor(12), 4)
        self.assertEqual(divisor(13), 1)
        self.assertEqual(divisor(14), 2)
        self.assertEqual(divisor(15), 4)
        self.assertEqual(divisor(16), 3)
        self.assertEqual(divisor(17), 1)
        self.assertEqual(divisor(18), 2)
        self.assertEqual(divisor(19), 1)
        self.assertEqual(divisor(20), 2)

    def test_divisor_negative(self):
        with self.assertRaises(TypeError):
            divisor(-1)

    def test_divisor_non_integer(self):
        with self.assertRaises(TypeError):
            divisor(3.5)
