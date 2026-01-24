import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(rombus_area(5, 10), 25.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(rombus_area(0, 10), 0)
        self.assertAlmostEqual(rombus_area(5, 0), 0)
        self.assertAlmostEqual(rombus_area(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rombus_area("5", 10)
        with self.assertRaises(TypeError):
            rombus_area(5, "10")
        with self.assertRaises(TypeError):
            rombus_area("5", "10")
