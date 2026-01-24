import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rombus_area(3, 4), 6.0)

    def test_edge_case_zero(self):
        self.assertEqual(rombus_area(0, 4), 0.0)
        self.assertEqual(rombus_area(3, 0), 0.0)

    def test_edge_case_one(self):
        self.assertEqual(rombus_area(1, 1), 0.5)

    def test_boundary_case_negative(self):
        self.assertEqual(rombus_area(-3, 4), 6.0)
        self.assertEqual(rombus_area(3, -4), 6.0)
