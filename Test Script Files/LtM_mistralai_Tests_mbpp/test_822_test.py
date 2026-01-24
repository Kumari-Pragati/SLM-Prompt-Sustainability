import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):

    def test_simple_valid_passwords(self):
        self.assertTrue(pass_validity("a1b2C3$"))
        self.assertTrue(pass_validity("A1B2c3#"))
        self.assertTrue(pass_validity("Ab1c2D3@"))
        self.assertTrue(pass_validity("a1b2c3d4"))
        self.assertTrue(pass_validity("A1B2C3D4"))
        self.assertTrue(pass_validity("Ab1C2D3E4"))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("123456"))
        self.assertFalse(pass_validity("A1B2C3D4E5"))
        self.assertFalse(pass_validity("Ab1C2D3E4F5"))
        self.assertFalse(pass_validity("a1b2c3d4e5"))
        self.assertFalse(pass_validity("A1B2C3D4E5F6"))
        self.assertFalse(pass_validity("Ab1C2D3E4F5G6"))
        self.assertFalse(pass_validity("a1b2c3d4e5f6"))
        self.assertFalse(pass_validity("A1B2C3D4E5F6G7"))
        self.assertFalse(pass_validity("Ab1C2D3E4F5G6H7"))

    def test_special_characters(self):
        self.assertTrue(pass_validity("a1b2C3$"))
        self.assertTrue(pass_validity("A1B2c3#"))
        self.assertTrue(pass_validity("Ab1c2D3@"))
        self.assertTrue(pass_validity("a1b2c3d4!"))
        self.assertTrue(pass_validity("A1B2C3D4%"))
        self.assertTrue(pass_validity("Ab1C2D3E4&"))
        self.assertTrue(pass_validity("a1b2c3d4e5*"))
        self.assertTrue(pass_validity("A1B2C3D4E5+"))
        self.assertTrue(pass_validity("Ab1C2D3E4F5-"))
        self.assertTrue(pass_validity("a1b2c3d4e5f6_"))
        self.assertTrue(pass_validity("A1B2C3D4E5F6G7`"))
        self.assertTrue(pass_validity("Ab1C2D3E4F5G6H7~"))

    def test_whitespace(self):
        self.assertFalse(pass_validity(" a1b2C3$ "))
        self.assertFalse(pass_validity(" A1B2c3# "))
        self.assertFalse(pass_validity(" Ab1c2D3@ "))
        self.assertFalse(pass_validity(" a1b2c3d4!"))
        self.assertFalse(pass_validity(" A1B2C3D4% "))
        self.assertFalse(pass_validity(" Ab1C2D3E4& "))
        self.assertFalse(pass_validity(" a1b2c3d4e5* "))
        self.assertFalse(pass_validity(" A1B2C3D4E5+ "))
        self.assertFalse(pass_validity(" Ab1C2D3E4F5- "))
        self.assertFalse(pass_validity(" a1b2c3d4e5f6_ "))
        self.assertFalse(pass_validity(" A1B2C3D4E5F6G7` "))
        self.assertFalse(pass_validity(" Ab1C2D3E4F5G6H7~ "))
