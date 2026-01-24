import unittest
from mbpp_358_code import moddiv_list

class TestModDivList(unittest.TestCase):

    def test_moddiv_list(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 3, 4]), [1, 2, 0])
        self.assertEqual(moddiv_list([10, 20, 30], [5, 5, 5]), [0, 0, 0])
        self.assertEqual(moddiv_list([10, 20, 30], [1, 2, 3]), [0, 0, 1])
        self.assertEqual(moddiv_list([10, 20, 30], [4, 4, 4]), [2, 2, 0])
        self.assertEqual(moddiv_list([10, 20, 30], [10, 20, 30]), [0, 0, 0])

    def test_moddiv_list_empty_list(self):
        self.assertEqual(moddiv_list([], []), [])

    def test_moddiv_list_diff_len(self):
        self.assertEqual(moddiv_list([10, 20], [2, 3, 4]), [1, 2])
