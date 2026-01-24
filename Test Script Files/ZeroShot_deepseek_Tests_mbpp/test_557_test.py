import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_toggle_string(self):
        self.assertEqual(toggle_string('Hello World'), 'hELLO wORLD')
        self.assertEqual(toggle_string('Python Programming'), 'pYTHON pROGRAMMING')
        self.assertEqual(toggle_string('123456'), '123456')
        self.assertEqual(toggle_string(''), '')
        self.assertEqual(toggle_string('aBcD'), 'AbCd')
