import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCorrespondingNum(unittest.TestCase):

    def test_empty_base(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, [], 10)
        self.assertRaises(ValueError, basesnum_coresspondingnum, (1,), 10)

    def test_empty_index(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, (2, 3, 5), [])
        self.assertRaises(ValueError, basesnum_coresspondingnum, (2, 3, 5), [0])

    def test_single_base(self):
        self.assertEqual(basesnum_coresspondingnum([2], [10]), [1024])
        self.assertEqual(basesnum_coresspondingnum([16], [4]), [65536])

    def test_multiple_bases(self):
        self.assertEqual(basesnum_coresspondingnum([2, 8], [2, 3]), [4, 512])
        self.assertEqual(basesnum_coresspondingnum([10, 16], [4, 5]), [16843009, 65536])

    def test_negative_base(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, [-2], [10])

    def test_negative_index(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, (2,), [-10])

    def test_base_greater_than_36(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, [37], [10])

    def test_index_greater_than_36(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, (2,), [37])
