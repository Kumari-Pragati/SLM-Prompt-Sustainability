import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_boundary_case(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_edge_case(self):
        self.assertEqual(rombus_perimeter(1), 4)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            rombus_perimeter(-1)

    def test_non_numeric_case(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('a')
