import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abccba'), 6)

    def test_edge_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends('a'), 1)

    def test_boundary_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends(''), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(123)
