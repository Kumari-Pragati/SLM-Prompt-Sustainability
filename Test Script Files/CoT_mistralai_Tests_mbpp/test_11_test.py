import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_single_character(self):
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("A", "a"), "A")

    def test_multiple_characters(self):
        self.assertEqual(remove_Occ("aaa", "a"), "")
        self.assertEqual(remove_Occ("AAA", "a"), "AAA")
        self.assertEqual(remove_Occ("aaBa", "a"), "B")
        self.assertEqual(remove_Occ("AaBa", "a"), "AaB")

    def test_edge_cases(self):
        self.assertEqual(remove_Occ("a", ""), "")
        self.assertEqual(remove_Occ("", "a"), "")
        self.assertEqual(remove_Occ("a", None), "")
        self.assertEqual(remove_Occ(None, "a"), None)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_Occ, 1, "a")
        self.assertRaises(TypeError, remove_Occ, "a", 1)
