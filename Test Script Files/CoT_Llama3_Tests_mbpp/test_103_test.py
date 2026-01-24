import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_eulerian_num_typical(self):
        self.assertEqual(eulerian_num(5, 3), 10)

    def test_eulerian_num_edge_case1(self):
        self.assertEqual(eulerian_num(0, 0), 1)

    def test_eulerian_num_edge_case2(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_eulerian_num_edge_case3(self):
        self.assertEqual(eulerian_num(5, 5), 0)

    def test_eulerian_num_invalid_input1(self):
        with self.assertRaises(TypeError):
            eulerian_num('a', 3)

    def test_eulerian_num_invalid_input2(self):
        with self.assertRaises(TypeError):
            eulerian_num(5, 'b')

    def test_eulerian_num_invalid_input3(self):
        with self.assertRaises(TypeError):
            eulerian_num('a', 'b')
