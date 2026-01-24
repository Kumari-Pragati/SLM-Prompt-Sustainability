import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_edge_cases(self):
        self.assertEqual(rombus_perimeter(0), 0)
        self.assertEqual(rombus_perimeter(1), 4)
        self.assertEqual(rombus_perimeter(2), 8)

    def test_negative_input(self):
        self.assertEqual(rombus_perimeter(-1), None)

    def test_non_integer_input(self):
        self.assertEqual(rombus_perimeter(3.14), None)
