import unittest
from mbpp_368_code import repeat_tuples

class TestRepeatTuples(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(repeat_tuples((1, 2), 3), ((1, 2), (1, 2), (1, 2)))
        self.assertEqual(repeat_tuples((3, 'a'), 2), ((3, 'a'), (3, 'a')))

    def test_edge_cases(self):
        self.assertEqual(repeat_tuples((1, 2), 0), ())
        self.assertEqual(repeat_tuples((1, 2), 1), ((1, 2)))
        self.assertEqual(repeat_tuples((1, 2), -1), ())

    def test_boundary_cases(self):
        self.assertEqual(repeat_tuples((1,), 1000000), ((1,), (1,), (1,) * 999999))
        self.assertEqual(repeat_tuples((1,), -1000000), ((1,),))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, repeat_tuples, (1, 2, 3), 'string')
        self.assertRaises(TypeError, repeat_tuples, 1, 2, 3)
