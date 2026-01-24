import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removezero_ip('192.168.0.1'), '192.168.0.1')

    def test_multiple_consecutive_zeros(self):
        self.assertEqual(removezero_ip('192.168.0.001'), '192.168.0.1')

    def test_single_zero(self):
        self.assertEqual(removezero_ip('192.168.0.10'), '192.168.0.10')

    def test_leading_zeros(self):
        self.assertEqual(removezero_ip('192.168.00.1'), '192.168.0.1')

    def test_single_digit_ip(self):
        self.assertEqual(removezero_ip('1.1.1.1'), '1.1.1.1')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removezero_ip(192.168.0.1)
