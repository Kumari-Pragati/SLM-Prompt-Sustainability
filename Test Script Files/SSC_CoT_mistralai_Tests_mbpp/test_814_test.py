import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_rombus_area_normal(self):
        self.assertEqual(rombus_area(3, 4), 6.0)
        self.assertEqual(rombus_area(5, 5), 12.5)

    def test_rombus_area_edge_cases(self):
        self.assertEqual(rombus_area(0, 4), 0.0)
        self.assertEqual(rombus_area(4, 0), 0.0)
        self.assertEqual(rombus_area(1, 1), 0.5)

    def test_rombus_area_negative(self):
        self.assertRaises(ValueError, rombus_area, -3, 4)
        self.assertRaises(ValueError, rombus_area, 3, -4)
