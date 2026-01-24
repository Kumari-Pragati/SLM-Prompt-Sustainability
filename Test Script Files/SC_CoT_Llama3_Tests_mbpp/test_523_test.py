import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(check_string('HelloWorld123'), ['Valid string.'])
        self.assertEqual(check_string('helloWorld12345'), ['Valid string.'])
        self.assertEqual(check_string('Hello123World'), ['Valid string.'])

    def test_edge_cases(self):
        self.assertEqual(check_string('HelloWorld'), ['String must have 1 number.', 'String must have 1 lower case character.', 'String must have 1 upper case character.'])
        self.assertEqual(check_string('helloWorld123'), ['String must have 1 upper case character.', 'String must have 1 lower case character.'])
        self.assertEqual(check_string('HELLO123'), ['String must have 1 lower case character.', 'String must have 1 upper case character.'])

    def test_special_cases(self):
        self.assertEqual(check_string(''), ['String length should be atleast 8.', 'String must have 1 lower case character.', 'String must have 1 upper case character.'])
        self.assertEqual(check_string('Hello'), ['String length should be atleast 8.', 'String must have 1 lower case character.', 'String must have 1 upper case character.'])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_string(None)
        with self.assertRaises(TypeError):
            check_string(123)
