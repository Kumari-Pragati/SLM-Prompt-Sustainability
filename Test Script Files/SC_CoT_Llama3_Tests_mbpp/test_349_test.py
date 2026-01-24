import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(check("101"), "Yes")
        self.assertEqual(check("111"), "Yes")
        self.assertEqual(check("000"), "Yes")
        self.assertEqual(check("110"), "No")

    def test_edge_cases(self):
        self.assertEqual(check("10"), "No")
        self.assertEqual(check("11"), "Yes")
        self.assertEqual(check("01"), "No")
        self.assertEqual(check("00"), "Yes")

    def test_boundary_cases(self):
        self.assertEqual(check("100"), "No")
        self.assertEqual(check("101"), "Yes")
        self.assertEqual(check("110"), "No")
        self.assertEqual(check("111"), "Yes")

    def test_special_cases(self):
        self.assertEqual(check(""), "No")
        self.assertEqual(check("1"), "No")
        self.assertEqual(check("0"), "Yes")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check(123)
