import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lower_ctr('HelloWorld'), 2)

    def test_all_lowercase(self):
        self.assertEqual(lower_ctr('helloworld'), 10)

    def test_no_lowercase(self):
        self.assertEqual(lower_ctr('HELLOWORLD'), 0)

    def test_mixed_case(self):
        self.assertEqual(lower_ctr('HelloWORLD'), 1)

    def test_empty_string(self):
        self.assertEqual(lower_ctr(''), 0)

    def test_special_characters(self):
        self.assertEqual(lower_ctr('Hello@World'), 2)

    def test_numbers_and_letters(self):
        self.assertEqual(lower_ctr('Hello123World456'), 2)

    def test_whitespace(self):
        self.assertEqual(lower_ctr('Hello World'), 2)
