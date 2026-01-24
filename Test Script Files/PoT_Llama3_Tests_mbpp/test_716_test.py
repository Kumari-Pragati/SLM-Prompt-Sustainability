import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_edge(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_edge2(self):
        self.assertEqual(rombus_perimeter(-5), 20)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            rombus_perimeter('a')
