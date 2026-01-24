import unittest
from mbpp_523_code import check_string

class TestCheckString(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check_string('aB1'), ['Valid string.'])
        self.assertEqual(check_string('Abcdefg1'), ['Valid string.'])

    def test_edge_cases(self):
        self.assertEqual(check_string('abcdefg'), 
                         ['String must have 1 upper case character.'])
        self.assertEqual(check_string('ABCDEFG'), 
                         ['String must have 1 lower case character.'])
        self.assertEqual(check_string('abcdefG'), 
                         ['String must have 1 upper case character.'])
        self.assertEqual(check_string('ABCdefg'), 
                         ['String must have 1 lower case character.'])
        self.assertEqual(check_string('ABCDEF'), 
                         ['String must have 1 number.'])
        self.assertEqual(check_string('abcdef'), 
                         ['String must have 1 upper case character.', 
                          'String must have 1 lower case character.', 
                          'String must have 1 number.'])

    def test_boundary_conditions(self):
        self.assertEqual(check_string('aB1' * 1000), ['Valid string.'])
        self.assertEqual(check_string('abcdefg' * 1000), 
                         ['String length should be atleast 8.'])
        self.assertEqual(check_string('ABCDEFG' * 1000), 
                         ['String length should be atleast 8.'])
        self.assertEqual(check_string('abcdefG' * 1000), 
                         ['String length should be atleast 8.'])
        self.assertEqual(check_string('ABCdefg' * 1000), 
                         ['String length should be atleast 8.'])
        self.assertEqual(check_string('ABCDEF' * 1000), 
                         ['String length should be atleast 8.'])
