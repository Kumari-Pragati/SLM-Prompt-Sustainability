import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))
        self.assertEqual(set_to_tuple({'a', 'b', 'c'}), ('a', 'b', 'c'))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(set_to_tuple({0}), (0,))
        self.assertEqual(set_to_tuple({1, 0}), (0, 1))
        self.assertEqual(set_to_tuple({'z', 'a', 'z'}), ('a', 'z'))
        self.assertEqual(set_to_tuple({'a', 'z', 'a'}), ('a', 'z'))

    def test_special_cases(self):
        self.assertEqual(set_to_tuple({None}), (None,))
        self.assertEqual(set_to_tuple({True, False}), (False, True))
        self.assertEqual(set_to_tuple({'', ' '}), ('', ''))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, set_to_tuple, 123)
        self.assertRaises(TypeError, set_to_tuple, (1, 2, 3))
