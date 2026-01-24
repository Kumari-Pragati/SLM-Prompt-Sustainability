import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(div_list([10, 20, 30], [1, 2, 3]), [10.0, 10.0, 10.0])

    def test_edge_condition(self):
        self.assertEqual(div_list([0], [1]), [0.0])

    def test_boundary_condition(self):
        self.assertEqual(div_list([1], [0]), [float('inf')])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            div_list([1, 2, 3], 'a')

        with self.assertRaises(TypeError):
            div_list('a', [1, 2, 3])

        with self.assertRaises(ZeroDivisionError):
            div_list([1, 2, 3], [0, 0, 0])
