import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_replica((1, 2, 3, 2)), (1, 2, 3))
        self.assertEqual(remove_replica((3, 2, 1)), (3, 'MSP'))
        self.assertEqual(remove_replica((1, 1, 2, 3)), (1, 2, 3))
        self.assertEqual(remove_replica((2, 2, 3, 2)), ('MSP', 3))

    def test_edge_case(self):
        self.assertEqual(remove_replica(()), ('MSP',))
        self.assertEqual(remove_replica((1,)), ('MSP',))
        self.assertEqual(remove_replica((1, 2)), ('MSP',))
        self.assertEqual(remove_replica((1, 2, 1)), (1, 2))

    def test_corner_case(self):
        self.assertEqual(remove_replica((1, 1, 1, 1)), (1,))
        self.assertEqual(remove_replica((1, 1, 1, 2)), (1, 2))
        self.assertEqual(remove_replica((1, 1, 'MSP', 1)), (1, 'MSP', 1))
