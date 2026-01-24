import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(removezero_ip('123.45.67.89'), '123.45.67.89')
        self.assertEqual(removezero_ip('123.0.0.0'), '123.0.0')
        self.assertEqual(removezero_ip('123.45.67.0'), '123.45.67')
        self.assertEqual(removezero_ip('123.0.0.9'), '123.0.0.9')

    def test_edge_cases(self):
        self.assertEqual(removezero_ip('0.0.0.0'), '.')
        self.assertEqual(removezero_ip('123.45.67.999'), '123.45.67.999')
        self.assertEqual(removezero_ip('123.45.67.255'), '123.45.67.255')
        self.assertEqual(removezero_ip('123.45.67.256'), '123.45.67.256')
        self.assertEqual(removezero_ip('123.45.67.256.8'), '123.45.67.256')
