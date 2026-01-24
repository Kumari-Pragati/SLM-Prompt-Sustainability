import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(check("0101"), "Yes")
        self.assertEqual(check("1010"), "Yes")
        self.assertEqual(check("0000"), "Yes")
        self.assertEqual(check("1111"), "Yes")

    def test_edge_conditions(self):
        self.assertEqual(check(""), "Yes")
        self.assertEqual(check("0"), "Yes")
        self.assertEqual(check("1"), "Yes")

    def test_boundary_conditions(self):
        self.assertEqual(check("01"), "Yes")
        self.assertEqual(check("10"), "Yes")
        self.assertEqual(check("0011"), "Yes")
        self.assertEqual(check("1100"), "Yes")

    def test_invalid_inputs(self):
        self.assertEqual(check("2101"), "No")
        self.assertEqual(check("101a"), "No")
        self.assertEqual(check("12345"), "No")
