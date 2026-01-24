import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_number_ctr_with_numbers(self):
        self.assertEqual(number_ctr('1234567890'), 10)

    def test_number_ctr_with_letters(self):
        self.assertEqual(number_ctr('abcdefghijklmnopqrstuvwxyz'), 0)

    def test_number_ctr_with_mix(self):
        self.assertEqual(number_ctr('abc123def456'), 6)

    def test_number_ctr_with_empty_string(self):
        self.assertEqual(number_ctr(''), 0)
