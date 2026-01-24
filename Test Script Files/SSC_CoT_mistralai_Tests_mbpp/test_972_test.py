import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_edge_input_1(self):
        self.assertEqual(concatenate_nested((1,), (2, 3, 4)), (1, 2, 3, 4))

    def test_edge_input_2(self):
        self.assertEqual(concatenate_nested((1, 2), (3,)), (1, 2, 3))

    def test_edge_input_3(self):
        self.assertEqual(concatenate_nested((1,), (2,)), (1, 2))

    def test_edge_input_4(self):
        self.assertEqual(concatenate_nested((1, 2), (3,)), (1, 2, 3))

    def test_edge_input_5(self):
        self.assertEqual(concatenate_nested((1,), (2, 3)), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(concatenate_nested((), (1, 2, 3)), (1, 2, 3))
        self.assertEqual(concatenate_nested((1, 2, 3),()), (1, 2, 3))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            concatenate_nested('a', 'b')
