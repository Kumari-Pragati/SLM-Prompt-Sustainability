import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_moddiv_list(self):
        self.assertEqual(moddiv_list([10, 20, 30], [3, 5, 7]), [1, 4, 4])
        self.assertEqual(moddiv_list([100, 200, 300], [10, 20, 30]), [0, 0, 0])
        self.assertEqual(moddiv_list([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [0, 0, 0, 0, 0])
        self.assertEqual(moddiv_list([1, 2, 3, 4, 5], [2]), [1, 0, 1, 0, 1])
        self.assertEqual(moddiv_list([], []), [])

        with self.assertRaises(TypeError):
            moddiv_list([10, 20, 30], 100)

        with self.assertRaises(TypeError):
            moddiv_list(100, [10, 20, 30])

        with self.assertRaises(ZeroDivisionError):
            moddiv_list([10, 20, 30], [0, 0, 0])
