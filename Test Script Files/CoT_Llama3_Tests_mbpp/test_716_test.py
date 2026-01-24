import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(rombus_perimeter(5), 20)
        self.assertEqual(rombus_perimeter(10), 40)
        self.assertEqual(rombus_perimeter(15), 60)

    def test_edge_cases(self):
        self.assertEqual(rombus_perimeter(0), 0)
        self.assertEqual(rombus_perimeter(-5), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('a')
        with self.assertRaises(TypeError):
            rombus_perimeter(None)
