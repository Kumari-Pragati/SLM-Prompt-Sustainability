import unittest
from mbpp_349_code import check

class TestCheck(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(check("0110"), "Yes")
        self.assertEqual(check("1010"), "Yes")
        self.assertEqual(check("1111"), "Yes")
        self.assertEqual(check("0000"), "Yes")

    def test_edge(self):
        self.assertEqual(check("0"), "Yes")
        self.assertEqual(check("1"), "Yes")
        self.assertEqual(check("01"), "Yes")
        self.assertEqual(check("10"), "Yes")

    def test_corner(self):
        self.assertEqual(check("111"), "No")
        self.assertEqual(check("000"), "No")
        self.assertEqual(check("101"), "No")
        self.assertEqual(check("010"), "No")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            check(123)
