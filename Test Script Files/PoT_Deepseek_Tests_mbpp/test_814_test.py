import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(rombus_area(5, 10), 25.0)

    def test_edge_case(self):
        self.assertAlmostEqual(rombus_area(0, 10), 0.0)
        self.assertAlmostEqual(rombus_area(5, 0), 0.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(rombus_area(1, 1), 0.5)
        self.assertAlmostEqual(rombus_area(1000000000000, 1000000000000), 5000000000000000000000.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rombus_area("5", 10)
        with self.assertRaises(TypeError):
            rombus_area(5, "10")
        with self.assertRaises(TypeError):
            rombus_area("5", "10")
