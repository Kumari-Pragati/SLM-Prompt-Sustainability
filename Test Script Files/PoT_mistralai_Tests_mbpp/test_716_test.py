import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rombus_perimeter(3), 12)

    def test_edge_case_zero(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(rombus_perimeter(1), 4)

    def test_boundary_case_small(self):
        self.assertEqual(rombus_perimeter(1.5), 6)

    def test_boundary_case_large(self.test_typical_case)
