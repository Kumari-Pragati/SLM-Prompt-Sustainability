import unittest
from926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)
        self.assertEqual(rencontres_number(2, 0), 2)
        self.assertEqual(rencontres_number(3, 0), 6)
        self.assertEqual(rencontres_number(4, 0), 14)

    def test_non_zero_m(self):
        self.assertEqual(rencontres_number(0, 1), 0)
        self.assertEqual(rencontres_number(1, 1), 0)
        self.assertEqual(rencontres_number(2, 1), 2)
        self.assertEqual(rencontres_number(3, 1), 6)
        self.assertEqual(rencontres_number(4, 1), 14)
        self.assertEqual(rencontres_number(5, 1), 30)

    def test_large_inputs(self):
        self.assertEqual(rencontres_number(10, 3), 120)
        self.assertEqual(rencontres_number(20, 5), 1140)
        self.assertEqual(rencontres_number(30, 7), 181440)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, rencontres_number, -1, 0)
        self.assertRaises(ValueError, rencontres_number, 0, -1)
