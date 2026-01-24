import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):

    def test_alphanumeric_string(self):
        self.assertEqual(check_alphanumeric('abc123'), 'Accept')
        self.assertEqual(check_alphanumeric('abc123@'), 'Discard')
        self.assertEqual(check_alphanumeric('abc123#'), 'Discard')
        self.assertEqual(check_alphanumeric('abc123$'), 'Accept')
        self.assertEqual(check_alphanumeric('123'), 'Accept')
        self.assertEqual(check_alphanumeric('abc'), 'Accept')
        self.assertEqual(check_alphanumeric(''), 'Discard')
