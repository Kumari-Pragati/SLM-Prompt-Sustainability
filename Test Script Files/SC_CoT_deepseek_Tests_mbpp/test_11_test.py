import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_edge_case(self):
        self.assertEqual(remove_Occ("", "a"), "")
        self.assertEqual(remove_Occ("a", "a"), "")

    def test_corner_case(self):
        self.assertEqual(remove_Occ("aaaa", "a"), "")
        self.assertEqual(remove_Occ("abc", "d"), "abc")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_Occ(123, "a")
        with self.assertRaises(TypeError):
            remove_Occ("hello", 123)
