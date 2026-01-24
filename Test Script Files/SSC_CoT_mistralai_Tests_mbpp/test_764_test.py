import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(number_ctr('12345'), 5)
        self.assertEqual(number_ctr('123456789'), 9)
        self.assertEqual(number_ctr('1234567890'), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(number_ctr('0'), 1)
        self.assertEqual(number_ctr('9'), 1)
        self.assertEqual(number_ctr('10'), 1)
        self.assertEqual(number_ctr('-12345'), 5)
        self.assertEqual(number_ctr('12345Z'), 5)
        self.assertEqual(number_ctr('12345_'), 5)
        self.assertEqual(number_ctr('12345 '), 5)
        self.assertEqual(number_ctr('12345\t'), 5)
        self.assertEqual(number_ctr('12345\n'), 0)
        self.assertEqual(number_ctr('12345\r'), 0)

    def test_special_or_corner_cases(self):
        self.assertEqual(number_ctr('12345A'), 5)
        self.assertEqual(number_ctr('A12345'), 1)
        self.assertEqual(number_ctr('12345a'), 5)
        self.assertEqual(number_ctr('12345.'), 5)
        self.assertEqual(number_ctr('12345,'), 5)
        self.assertEqual(number_ctr('12345;'), 5)
        self.assertEqual(number_ctr('12345!"#$%&\'()*+,-./:@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'), 0)
