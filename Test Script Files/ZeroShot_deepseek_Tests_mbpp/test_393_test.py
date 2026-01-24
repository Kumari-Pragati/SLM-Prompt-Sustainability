import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_max_length_list(self):
        self.assertEqual(max_length_list(['abc', 'de', 'fghi']), (4, 'fghi'))
        self.assertEqual(max_length_list(['abc', 'de', 'fghi', 'j']), (4, 'fghi'))
        self.assertEqual(max_length_list(['abc', 'de', 'fgh', 'ijklm']), (5, 'ijklm'))
        self.assertEqual(max_length_list(['abc', 'de', 'fgh', 'ijkl']), (4, 'ijkl'))
        self.assertEqual(max_length_list(['abc', 'de', 'fgh', 'ij']), (3, 'fgh'))
        self.assertEqual(max_length_list(['abc', 'de', 'f', 'ij']), (2, 'ij'))
        self.assertEqual(max_length_list(['abc', 'd', 'f', 'ij']), (2, 'ij'))
        self.assertEqual(max_length_list(['abc', 'd', 'fgh', 'ij']), (3, 'fgh'))
        self.assertEqual(max_length_list(['abc', 'de', 'fgh', 'ijklmn']), (6, 'ijklmn'))
        self.assertEqual(max_length_list(['abc', 'de', 'fgh', 'ijklm']), (5, 'ijklm'))
