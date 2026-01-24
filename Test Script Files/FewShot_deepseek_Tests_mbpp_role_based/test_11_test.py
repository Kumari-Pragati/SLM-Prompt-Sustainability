import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_edge_condition(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_boundary_condition(self):
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("aaaa", "a"), "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_Occ(123, "a")
        with self.assertRaises(TypeError):
            remove_Occ("hello", 123)
