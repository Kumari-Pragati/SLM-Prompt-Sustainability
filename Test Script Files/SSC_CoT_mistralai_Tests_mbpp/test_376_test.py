import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(remove_replica((1, 2, 3, 4)), (1, 2, 3))
        self.assertListEqual(remove_replica((4, 3, 2, 1)), (4, 3))
        self.assertListEqual(remove_replica((1, 1, 2, 3)), (2, 3))

    def test_edge_input(self):
        self.assertListEqual(remove_replica((1,)), (1,))
        self.assertListEqual(remove_replica((1, 1, 1)), (1,))
        self.assertListEqual(remove_replica((1, 1, 1, 2)), (2,))
        self.assertListEqual(remove_replica((1, 1, 1, 1, 2)), (2,))

    def test_boundary_input(self):
        self.assertListEqual(remove_replica((0, 1, 2)), (0, 1, 2))
        self.assertListEqual(remove_replica((-1, 0, 1)), (-1, 0, 1))
        self.assertListEqual(remove_replica((1, 2, 3, 4, 5)), (1, 2, 3, 4))
        self.assertListEqual(remove_replica((5, 4, 3, 2, 1)), (5, 4, 3, 2))

    def test_invalid_input(self):
        self.assertListEqual(remove_replica(('a', 'b', 'c')), ('MSP', 'MSP', 'MSP'))
        self.assertListEqual(remove_replica([1, 2, 3]), ('MSP', 'MSP', 'MSP'))
        self.assertListEqual(remove_replica({1, 2, 3}), ('MSP', 'MSP', 'MSP'))
