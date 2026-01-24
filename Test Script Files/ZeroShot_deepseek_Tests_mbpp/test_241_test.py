import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_array_3d(self):
        result = array_3d(2, 3, 4)
        self.assertEqual(len(result), 4)
        for i in range(4):
            self.assertEqual(len(result[i]), 3)
            for j in range(3):
                self.assertEqual(len(result[i][j]), 2)
                for k in range(2):
                    self.assertEqual(result[i][j][k], '*')
