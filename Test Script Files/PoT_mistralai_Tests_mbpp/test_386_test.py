import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('[()()]'), 0)
        self.assertEqual(swap_count('[()][{}]'), 1)
        self.assertEqual(swap_count('[()][{}([])}'), 1)
        self.assertEqual(swap_count('[()][{}([{}[()])}]'), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('()'), 0)
        self.assertEqual(swap_count('[][]'), 0)
        self.assertEqual(swap_count('()()'), 0)
        self.assertEqual(swap_count('()[]'), 1)
        self.assertEqual(swap_count('[()]'), 1)
        self.assertEqual(swap_count('[()][{}]'), 1)
        self.assertEqual(swap_count('[()][{}([])}'), 1)
        self.assertEqual(swap_count('[()][{}([{}[()])}]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][][][][][][]'), 2)
        self.assertEqual(swap_count('[()][{}([{}[()])}][][][][][][][][][][][][][][][][][][][][]'),