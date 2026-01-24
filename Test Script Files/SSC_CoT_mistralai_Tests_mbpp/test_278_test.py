import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 0)
        self.assertEqual(count_first_elements(('a', 'b', (1, 2), 'd', 'e')), 0)
        self.assertEqual(count_first_elements([1, 2, (3, 4), 5, 6]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_first_elements(()), 0)
        self.assertEqual(count_first_elements((1,)), 0)
        self.assertEqual(count_first_elements((1, 2, (3,))), 2)
        self.assertEqual(count_first_elements((1, (2,), 3)), 0)
        self.assertEqual(count_first_elements((1, (2, (3,))),), 0)
        self.assertEqual(count_first_elements((1, (2, (3,)),)), 0)

    def test_special_cases(self):
        self.assertEqual(count_first_elements(((),)), 0)
        self.assertEqual(count_first_elements(((), 1)), 0)
        self.assertEqual(count_first_elements((1, ())), 1)
        self.assertEqual(count_first_elements((1, (), 2)), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_first_elements, 123)
        self.assertRaises(TypeError, count_first_elements, [1, 2, 3, '4'])
        self.assertRaises(TypeError, count_first_elements, {'a': 1, 'b': 2, (3, 4)})
