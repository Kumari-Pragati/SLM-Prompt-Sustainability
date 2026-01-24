import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 2)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(8), 8)

    def test_edge_and_boundary(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(15), 16)
        self.assertEqual(next_Power_Of_2(31), 32)
        self.assertEqual(next_Power_Of_2(127), 128)
        self.assertEqual(next_Power_Of_2(128), 128)
        self.assertEqual(next_Power_Of_2(129), 128)
        self.assertEqual(next_Power_Of_2(2147483647), 2147483680)

    def test_complex(self):
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(7), 8)
        self.assertEqual(next_Power_Of_2(9), 16)
        self.assertEqual(next_Power_Of_2(11), 16)
        self.assertEqual(next_Power_Of_2(13), 16)
        self.assertEqual(next_Power_Of_2(14), 16)
        self.assertEqual(next_Power_Of_2(16), 16)
        self.assertEqual(next_Power_Of_2(17), 32)
        self.assertEqual(next_Power_Of_2(19), 32)
        self.assertEqual(next_Power_Of_2(20), 32)
        self.assertEqual(next_Power_Of_2(21), 32)
        self.assertEqual(next_Power_Of_2(22), 32)
        self.assertEqual(next_Power_Of_2(23), 32)
        self.assertEqual(next_Power_Of_2(255), 256)
        self.assertEqual(next_Power_Of_2(256), 256)
        self.assertEqual(next_Power_Of_2(257), 256)
        self.assertEqual(next_Power_Of_2(258), 256)
        self.assertEqual(next_Power_Of_2(259), 256)
        self.assertEqual(next_Power_Of_2(260), 256)
        self.assertEqual(next_Power_Of_2(261), 256)
        self.assertEqual(next_Power_Of_2(262), 256)
        self.assertEqual(next_Power_Of_2(263), 256)
        self.assertEqual(next_Power_Of_2(264), 256)
        self.assertEqual(next_Power_Of_2(265), 256)
        self.assertEqual(next_Power_Of_2(266), 256)
        self.assertEqual(next_Power_Of_2(267), 256)
        self.assertEqual(next_Power_Of_2(268), 256)
        self.assertEqual(next_Power_Of_2(269), 256)
        self.assertEqual(next_Power_Of_2(270), 256)
        self.assertEqual(next_Power_Of_2(271), 256)
