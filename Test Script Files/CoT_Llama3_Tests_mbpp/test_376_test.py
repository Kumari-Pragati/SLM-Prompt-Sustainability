import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_replica((1, 2, 3, 2, 1)), ('MSP', 1, 2, 3))

    def test_edge_case(self):
        self.assertEqual(remove_replica(()), ())

    def test_edge_case2(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_edge_case3(self):
        self.assertEqual(remove_replica((1, 1, 1)), ('MSP',))

    def test_edge_case4(self):
        self.assertEqual(remove_replica((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_edge_case5(self):
        self.assertEqual(remove_replica((1, 2, 2, 3, 1)), (1, 2, 3))

    def test_edge_case6(self):
        self.assertEqual(remove_replica((1, 1, 2, 2, 3)), ('MSP', 1, 2, 3))

    def test_edge_case7(self):
        self.assertEqual(remove_replica((1, 1, 1, 1, 1)), ('MSP',))

    def test_edge_case8(self):
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_edge_case9(self):
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_edge_case10(self):
        self.assertEqual(remove_replica((1, 1, 1, 1, 1, 1, 1, 1, 1, 1)), ('MSP',))
