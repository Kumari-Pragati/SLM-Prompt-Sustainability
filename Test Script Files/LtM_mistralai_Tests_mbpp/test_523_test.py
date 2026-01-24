import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_simple_string(self):
        self.assertListEqual(check_string('AbCd1234'), ['Valid string.'])
        self.assertListEqual(check_string('aBcD123'), ['Valid string.'])
        self.assertListEqual(check_string('AbCd12345'), ['Valid string.'])

    def test_edge_cases(self):
        self.assertListEqual(check_string('AbCd123'), ['String length should be atleast 8.'])
        self.assertListEqual(check_string('AbCd'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.'])
        self.assertListEqual(check_string('1234567'), ['String must have 1 upper case character.', 'String must have 1 lower case character.', 'String must have 1 number.'])
        self.assertListEqual(check_string('ABCDEFG'), ['String must have 1 lower case character.', 'String must have 1 number.'])
        self.assertListEqual(check_string('AbCd1'), ['String length should be atleast 8.'])

    def test_complex_cases(self):
        self.assertListEqual(check_string('AbCd!123'), ['Valid string.'])
        self.assertListEqual(check_string('AbCd_123'), ['Valid string.'])
        self.assertListEqual(check_string('AbCd123456'), ['Valid string.'])
        self.assertListEqual(check_string('AbCd12345678'), ['Valid string.'])
        self.assertListEqual(check_string('AbCd123456789'), ['String length should be atleast 8.'])
