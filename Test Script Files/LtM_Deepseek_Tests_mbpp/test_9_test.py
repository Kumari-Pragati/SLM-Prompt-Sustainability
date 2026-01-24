import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    # Test for simple / typical inputs
    def test_simple_inputs(self):
        self.assertEqual(find_Rotations("abc"), 0)
        self.assertEqual(find_Rotations("abcdabcd"), 4)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(find_Rotations(""), 0)
        self.assertEqual(find_Rotations("a"), 0)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(find_Rotations("abcabc"), 0)
        self.assertEqual(find_Rotations("abcabca"), 1)
        self.assertEqual(find_Rotations("abcabcabc"), 0)
        self.assertEqual(find_Rotations("abcabcabca"), 1)
        self.assertEqual(find_Rotations("abcabcabcabc"), 0)
        self.assertEqual(find_Rotations("abcabcabcabcabca"), 1)
