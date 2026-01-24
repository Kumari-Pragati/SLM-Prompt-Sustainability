import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_bell_number_0(self):
        self.assertEqual(bell_Number(0), 1)

    def test_bell_number_1(self):
        self.assertEqual(bell_Number(1), 1)

    def test_bell_number_2(self):
        self.assertEqual(bell_Number(2), 2)

    def test_bell_number_3(self):
        self.assertEqual(bell_Number(3), 4)

    def test_bell_number_4(self):
        self.assertEqual(bell_Number(4), 10)

    def test_bell_number_5(self):
        self.assertEqual(bell_Number(5), 20)

    def test_bell_number_large(self):
        self.assertEqual(bell_Number(100), 3542248481792619150)
