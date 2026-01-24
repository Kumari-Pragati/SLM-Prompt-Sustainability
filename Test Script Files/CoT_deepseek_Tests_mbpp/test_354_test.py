import unittest
from mbpp_354_code import tn_ap

class TestTNAP(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tn_ap(5, 10, 2), 25)

    def test_zero_difference(self):
        self.assertEqual(tn_ap(5, 10, 0), 5)

    def test_negative_difference(self):
        self.assertEqual(tn_ap(5, 10, -2), -9)

    def test_negative_start(self):
        self.assertEqual(tn_ap(-5, 10, 2), 15)

    def test_large_numbers(self):
        self.assertEqual(tn_ap(1000000, 10, 2), 2000010)

    def test_zero_n(self):
        self.assertEqual(tn_ap(5, 0, 2), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tn_ap("a", 10, 2)
        with self.assertRaises(TypeError):
            tn_ap(5, "b", 2)
        with self.assertRaises(TypeError):
            tn_ap(5, 10, "c")
