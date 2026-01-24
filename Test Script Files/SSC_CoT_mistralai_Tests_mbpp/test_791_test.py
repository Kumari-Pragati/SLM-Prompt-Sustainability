import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_nested((1, 2, (3, 4), 5)), (1, 2, 5))
        self.assertEqual(remove_nested((1, (2, (3, 4)), 5)), (1, 2, 5))
        self.assertEqual(remove_nested(((1, 2), (3, 4), 5)), (1, 2, 3, 4, 5))

    def test_edge_cases(self):
        self.assertEqual(remove_nested((1,)), (1,))
        self.assertEqual(remove_nested((1, ())), (1,))
        self.assertEqual(remove_nested(((1,),)), (1,))
        self.assertEqual(remove_nested(((),)), ())
        self.assertEqual(remove_nested(((), 1)), (1,))
        self.assertEqual(remove_nested(((1,), (2,))), (1, 2))

    def test_boundary_cases(self):
        self.assertEqual(remove_nested((1, 2, 3, (4,), 5)), (1, 2, 3, 5))
        self.assertEqual(remove_nested((1, (2,), 3, (4,), 5)), (1, 2, 3, 5))
        self.assertEqual(remove_nested((1, (2, 3), (4,), 5)), (1, 2, 3, 5))
        self.assertEqual(remove_nested((1, (2, 3, 4), 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_nested((1, 2, (3, 4, 5), 6)), (1, 2, 3, 4, 5, 6))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_nested, 123)
        self.assertRaises(TypeError, remove_nested, [1, 2, 3])
        self.assertRaises(TypeError, remove_nested, (1, 2, '3'))
        self.assertRaises(TypeError, remove_nested, (1, (2,), {'3')))
