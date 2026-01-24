import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(check("aeiou"), "accepted")
        self.assertEqual(check("AeIoU"), "accepted")
        self.assertEqual(check("aEiOu"), "accepted")

    def test_edge_cases(self):
        self.assertEqual(check("aAEIOU"), "accepted")
        self.assertEqual(check("aAeIou"), "accepted")
        self.assertEqual(check("AaEiOu"), "accepted")
        self.assertEqual(check("AaEiou1"), "not accepted")
        self.assertEqual(check("Aa1Eiou"), "not accepted")
        self.assertEqual(check("AaEiou!"), "not accepted")

    def test_boundary_cases(self):
        self.assertEqual(check("AEIOU"), "not accepted")
        self.assertEqual(check("aeiou"), "not accepted")
        self.assertEqual(check("AeIou"), "not accepted")
        self.assertEqual(check("aEiOU"), "not accepted")
        self.assertEqual(check("aEiou"), "not accepted")
