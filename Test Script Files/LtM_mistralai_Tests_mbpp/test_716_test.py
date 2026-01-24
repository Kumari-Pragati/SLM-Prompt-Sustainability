import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(rombus_perimeter(1), 4)

    def test_edge_input(self):
        self.assertEqual(rombus_perimeter(0), 0)
        self.assertEqual(rombus_perimeter(1000000), 4000000)

    def test_complex_input(self):
        self.assertEqual(rombus_perimeter(2.5), 10)
        self.assertEqual(rombus_perimeter(-1), 0)
