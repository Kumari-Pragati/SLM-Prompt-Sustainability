import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(area_trapezium(5, 3, 4), 13.0)

    def test_zero_base(self):
        self.assertEqual(area_trapezium(0, 3, 4), 0)

    def test_zero_height(self):
        self.assertEqual(area_trapezium(5, 3, 0), 0)

    def test_negative_base(self):
        self.assertAlmostEqual(area_trapezium(-5, 3, 4), 13.0)

    def test_negative_height(self):
        self.assertEqual(area_trapezium(5, 3, -4), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            area_trapezium('a', 3, 4)
