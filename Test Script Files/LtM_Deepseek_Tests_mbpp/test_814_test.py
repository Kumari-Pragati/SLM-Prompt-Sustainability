import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(rombus_area(5, 10), 25.0)

    def test_zero_area(self):
        self.assertEqual(rombus_area(0, 10), 0)
        self.assertEqual(rombus_area(5, 0), 0)

    def test_negative_values(self):
        self.assertEqual(rombus_area(-5, 10), 0)
        self.assertEqual(rombus_area(5, -10), 0)
        self.assertEqual(rombus_area(-5, -10), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(rombus_area(10000000000, 20000000000), 100000000000000000000.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rombus_area("5", 10)
        with self.assertRaises(TypeError):
            rombus_area(5, "10")
        with self.assertRaises(TypeError):
            rombus_area("5", "10")
