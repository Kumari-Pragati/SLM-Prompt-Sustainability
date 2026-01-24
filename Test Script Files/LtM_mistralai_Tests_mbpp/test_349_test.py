import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_simple_single_digit(self):
        self.assertEqual(check("0"), "Yes")
        self.assertEqual(check("1"), "Yes")

    def test_simple_multiple_digits(self):
        self.assertEqual(check("00"), "Yes")
        self.assertEqual(check("11"), "Yes")
        self.assertEqual(check("011"), "No")
        self.assertEqual(check("100"), "No")

    def test_edge_cases(self):
        self.assertEqual(check("000"), "Yes")
        self.assertEqual(check("111"), "Yes")
        self.assertEqual(check("012"), "No")
        self.assertEqual(check("102"), "No")
        self.assertEqual(check("01"), "No")
        self.assertEqual(check("10"), "No")

    def test_boundary_cases(self):
        self.assertEqual(check("0000000"), "Yes")
        self.assertEqual(check("1111111"), "Yes")
        self.assertEqual(check("0123456"), "No")
        self.assertEqual(check("1023456"), "No")
        self.assertEqual(check("01"), "No")
        self.assertEqual(check("10"), "No")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check, 123)
        self.assertRaises(TypeError, check, [])
        self.assertRaises(TypeError, check, {})
        self.assertRaises(TypeError, check, None)
