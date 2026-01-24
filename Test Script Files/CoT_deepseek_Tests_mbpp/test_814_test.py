import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(rombus_area(10, 20), 100.0)

    def test_zero_input(self):
        self.assertEqual(rombus_area(0, 20), 0)
        self.assertEqual(rombus_area(10, 0), 0)

    def test_negative_input(self):
        self.assertEqual(rombus_area(-10, 20), 0)
        self.assertEqual(rombus_area(10, -20), 0)
        self.assertEqual(rombus_area(-10, -20), 0)

    def test_large_input(self):
        self.assertAlmostEqual(rombus_area(10000000000, 20000000000), 1.0e19)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rombus_area("10", 20)
        with self.assertRaises(TypeError):
            rombus_area(10, "20")
        with self.assertRaises(TypeError):
            rombus_area("10", "20")
