import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9), 10)

    def test_edge_case_start_end(self):
        self.assertEqual(find_First_Missing([0], 0, 0), 1)
        self.assertEqual(find_First_Missing([0, 1], 0, 1), 2)

    def test_corner_case_missing_in_middle(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 5, 6, 7, 8, 9], 0, 8), 4)

    def test_corner_case_missing_at_start(self):
        self.assertEqual(find_First_Missing([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8), 0)

    def test_corner_case_missing_at_end(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8], 0, 8), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_First_Missing("not an array", 0, 9)
        with self.assertRaises(TypeError):
            find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "not an integer", 9)
        with self.assertRaises(TypeError):
            find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, "not an integer")
