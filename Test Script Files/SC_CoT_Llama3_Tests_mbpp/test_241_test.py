import unittest
from mbpp_241_code import array_3d

class TestArray3d(unittest.TestCase):
    def test_typical_inputs(self):
        result = array_3d(2, 3, 4)
        self.assertEqual(len(result), 4)
        for i in range(4):
            self.assertEqual(len(result[i]), 3)
            for j in range(3):
                self.assertEqual(result[i][j], '*')

    def test_edge_case_m(self):
        result = array_3d(1, 3, 4)
        self.assertEqual(len(result), 4)
        for i in range(4):
            self.assertEqual(len(result[i]), 3)
            for j in range(3):
                self.assertEqual(result[i][j], '*')

    def test_edge_case_n(self):
        result = array_3d(2, 1, 4)
        self.assertEqual(len(result), 4)
        for i in range(4):
            self.assertEqual(len(result[i]), 1)
            for j in range(1):
                self.assertEqual(result[i][j], '*')

    def test_edge_case_o(self):
        result = array_3d(2, 3, 1)
        self.assertEqual(len(result), 1)
        for i in range(1):
            self.assertEqual(len(result[i]), 3)
            for j in range(3):
                self.assertEqual(result[i][j], '*')

    def test_invalid_input_m(self):
        with self.assertRaises(TypeError):
            array_3d('a', 3, 4)

    def test_invalid_input_n(self):
        with self.assertRaises(TypeError):
            array_3d(2, 'b', 4)

    def test_invalid_input_o(self):
        with self.assertRaises(TypeError):
            array_3d(2, 3, 'c')
