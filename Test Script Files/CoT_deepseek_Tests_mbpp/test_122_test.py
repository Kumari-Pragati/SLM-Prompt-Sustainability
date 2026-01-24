import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_boundary_conditions(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(MAX), 3000)

    def test_invalid_inputs(self):
        with self.assertRaises(IndexError):
            smartNumber(0)
        with self.assertRaises(IndexError):
            smartNumber(MAX + 1)
        with self.assertRaises(TypeError):
            smartNumber("1")
        with self.assertRaises(TypeError):
            smartNumber(None)
