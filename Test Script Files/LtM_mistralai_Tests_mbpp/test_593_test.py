import unittest
from mbpp_593_code import removezero_ip

class TestRemoveZeroIP(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(removezero_ip('123.456.789.0'), '123.456.789.')
        self.assertEqual(removezero_ip('123.0.0.0'), '123.')
        self.assertEqual(removezero_ip('0.0.0.0'), '')

    def test_edge_input(self):
        self.assertEqual(removezero_ip('123.456.789.255'), '123.456.789.')
        self.assertEqual(removezero_ip('123.456.789.256'), '123.456.789.256')
        self.assertEqual(removezero_ip('123.456.789.257'), '123.456.789.257')
        self.assertEqual(removezero_ip('123.456.789.258'), '123.456.789.258')
        self.assertEqual(removezero_ip('123.456.789.259'), '123.456.789.259')

    def test_complex_input(self):
        self.assertEqual(removezero_ip('123.456.789.255.0'), '123.456.789.255')
        self.assertEqual(removezero_ip('123.456.789.255.0.0'), '123.456.789.255')
        self.assertEqual(removezero_ip('123.456.789.255.0.0.0'), '123.456.789.255')
        self.assertEqual(removezero_ip('123.456.789.255.0.0.0.0'), '123.456.789.255')
        self.assertEqual(removezero_ip('123.456.789.255.0.0.0.0.0'), '123.456.789.255')
