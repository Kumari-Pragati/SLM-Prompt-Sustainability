import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(number_ctr('abc123def456'), 6)
        self.assertEqual(number_ctr('1234567890'), 10)
        self.assertEqual(number_ctr('abcdef'), 0)

    def test_edge_cases(self):
        self.assertEqual(number_ctr(''), 0)
        self.assertEqual(number_ctr('0'), 1)
        self.assertEqual(number_ctr('9'), 1)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any explicit error cases,
        # we can test with None and other non-string inputs
        self.assertIsNone(number_ctr(None))
        self.assertIsNone(number_ctr(123456))
        self.assertIsNone(number_ctr(['1', '2', '3']))
