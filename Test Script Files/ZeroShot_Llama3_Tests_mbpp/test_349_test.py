import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_check_function(self):
        self.assertEqual(check("101"), "Yes")
        self.assertEqual(check("010"), "Yes")
        self.assertEqual(check("111"), "Yes")
        self.assertEqual(check("000"), "Yes")
        self.assertEqual(check("100"), "No")
        self.assertEqual(check("110"), "No")
        self.assertEqual(check("001"), "No")
        self.assertEqual(check("1111"), "Yes")
        self.assertEqual(check("1010"), "No")
        self.assertEqual(check(""), "No")
