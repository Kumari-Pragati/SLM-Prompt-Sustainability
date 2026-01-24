import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(rombus_area(4, 6), 12.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(rombus_area(0, 6), 0.0)
        self.assertAlmostEqual(rombus_area(4, 0), 0.0)

    def test_edge_case(self):
        self.assertAlmostEqual(rombus_area(1, 1), 0.5)
        self.assertAlmostEqual(rombus_area(2, 4), 4.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rombus_area("4", 6)
        with self.assertRaises(TypeError):
            rombus_area(4, "6")
        with self.assertRaises(TypeError):
            rombus_area("4", "6")
