import unittest
from mbpp_598_code import armstrong_number

class TestArmstrongNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(armstrong_number(153))

    def test_typical_use_case_2(self):
        self.assertTrue(armstrong_number(370))

    def test_edge_case(self):
        self.assertTrue(armstrong_number(0))

    def test_boundary_case(self):
        self.assertFalse(armstrong_number(1000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            armstrong_number('153')

    def test_negative_number(self):
        self.assertFalse(armstrong_number(-153))
