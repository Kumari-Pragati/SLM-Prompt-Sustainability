import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)
        self.assertEqual(multiply_list([4, 5, 6]), 120)
        self.assertEqual(multiply_list([-1, 2, 3]), -3)

    def test_edge_cases(self):
        self.assertEqual(multiply_list([]), 1)
        self.assertEqual(multiply_list([0]), 0)
        self.assertEqual(multiply_list([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3]), 6)
        self.assertEqual(multiply_list([-4, -5, -6]), 120)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            multiply_list([1, '2', 3])

    def test_single_element_list(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_large_numbers(self):
        self.assertEqual(multiply_list([100, 200, 300]), 60000000)
