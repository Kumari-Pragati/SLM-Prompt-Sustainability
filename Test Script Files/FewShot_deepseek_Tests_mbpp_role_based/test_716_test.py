import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_boundary_conditions(self):
        self.assertEqual(rombus_perimeter(0), 0)
        self.assertEqual(rombus_perimeter(1), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('a')
        with self.assertRaises(ValueError):
            rombus_perimeter(-5)
