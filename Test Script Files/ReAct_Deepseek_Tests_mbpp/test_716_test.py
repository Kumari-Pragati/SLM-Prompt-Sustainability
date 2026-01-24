import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_zero_case(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            rombus_perimeter(-5)

    def test_large_number_case(self):
        self.assertEqual(rombus_perimeter(10000), 40000)
