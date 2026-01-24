import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_cases(self):
        self.assertFalse(check_Validity(0, 0, 0))
        self.assertFalse(check_Validity(1, 1, 2))
        self.assertFalse(check_Validity(1, 2, 1))
        self.assertFalse(check_Validity(2, 1, 1))
        self.assertFalse(check_Validity(1, 3, 2))
        self.assertFalse(check_Validity(2, 3, 1))

    def test_corner_cases(self):
        self.assertFalse(check_Validity(1, 2, 2))
        self.assertFalse(check_Validity(2, 2, 1))
        self.assertFalse(check_Validity(2, 1, 2))
        self.assertFalse(check_Validity(3, 3, 3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Validity("1", 2, 3)
        with self.assertRaises(TypeError):
            check_Validity(1, "2", 3)
        with self.assertRaises(TypeError):
            check_Validity(1, 2, "3")
        with self.assertRaises(TypeError):
            check_Validity("1", "2", "3")
        with self.assertRaises(TypeError):
            check_Validity(1.5, 2, 3)
        with self.assertRaises(TypeError):
            check_Validity(1, 2.5, 3)
        with self.assertRaises(TypeError):
            check_Validity(1, 2, 3.5)
        with self.assertRaises(TypeError):
            check_Validity(1.5, 2.5, 3)
        with self.assertRaises(TypeError):
            check_Validity(1.5, 2, 3.5)
        with self.assertRaises(TypeError):
            check_Validity(1, 2.5, 3.5)
