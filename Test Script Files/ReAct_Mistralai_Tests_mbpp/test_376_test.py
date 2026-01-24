import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_replica(()), ('MSP',))

    def test_single_element(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(remove_replica((1, 1, 2)), (1, 2))

    def test_multiple_elements(self):
        self.assertEqual(remove_replica((1, 2, 3, 1, 2)), (1, 2, 3))

    def test_boundary_case_one_element(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_boundary_case_two_elements(self):
        self.assertEqual(remove_replica((1, 2)), (1, 2))

    def test_boundary_case_many_elements(self):
        self.assertEqual(remove_replica((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_negative_elements(self):
        self.assertEqual(remove_replica((-1, -2, -3)), ())

    def test_mixed_elements(self):
        self.assertEqual(remove_replica((1, -2, 3, 1, -2)), (1, 3))

    def test_non_hashable_element(self):
        self.assertRaises(TypeError, remove_replica, ([1, 2, 3]))
