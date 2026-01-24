import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(fill_spaces("Hello, World."), "Hello:World:")
        self.assertEqual(fill_spaces("A, B, C, D"), "A:B:C:D")
        self.assertEqual(fill_spaces("1, 2, 3, 4"), "1:2:3:4")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(fill_spaces(""), "")
        self.assertEqual(fill_spaces("Hello:World."), "Hello:World:")
        self.assertEqual(fill_spaces("A, B, C, D,"), "A:B:C:D:")
        self.assertEqual(fill_spaces("A, B, C, D, E, F, G, H, I, J"), "A:B:C:D:E:F:G:H:I:J")
        self.assertEqual(fill_spaces("A, B, C, D, E, F, G, H, I, J, K"), "A:B:C:D:E:F:G:H:I:J:K")

    def test_special_and_corner_cases(self):
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
        self.assertEqual(fill_spaces("Hello, World?"), "Hello:World?")
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World!")
