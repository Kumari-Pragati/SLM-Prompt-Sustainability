import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(replace_spaces("hello world"), "h0l0l0e0w0l0d0r0d")
        self.assertEqual(replace_spaces(""), "")
        self.assertEqual(replace_spaces("a"), "a" )

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(replace_spaces("a b"), "a0b0" )
        self.assertEqual(replace_spaces("a b c"), "a0b0c0" )
        self.assertEqual(replace_spaces("a b c d"), "a0b0c0d0" )
        self.assertEqual(replace_spaces("a b c d e"), "a0b0c0d0e0" )
        self.assertEqual(replace_spaces("a b c d e f"), "a0b0c0d0e0f0" )
        self.assertEqual(replace_spaces("a b c d e f g"), "a0b0c0d0e0f0g0" )
        self.assertEqual(replace_spaces("a b c d e f g h"), "a0b0c0d0e0f0g0h0" )
        self.assertEqual(replace_spaces("a b c d e f g h i"), "a0b0c0d0e0f0g0h0i0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j"), "a0b0c0d0e0f0g0h0i0j0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k"), "a0b0c0d0e0f0g0h0i0j0k0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l"), "a0b0c0d0e0f0g0h0i0j0k0l0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m"), "a0b0c0d0e0f0g0h0i0j0k0l0m0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p0q0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p0q0r0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p0q0r0s0" )
        self.assertEqual(replace_spaces("a b c d e f g h i j k l m n o p q r s t"), "a0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p