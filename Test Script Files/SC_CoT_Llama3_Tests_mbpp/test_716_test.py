import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_edge_case_zero(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            rombus_perimeter(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('five')

    def test_edge_case_large_number(self):
        self.assertEqual(rombus_perimeter(1000), 4000)

    def test_edge_case_large_negative_number(self):
        with self.assertRaises(TypeError):
            rombus_perimeter(-1000)
