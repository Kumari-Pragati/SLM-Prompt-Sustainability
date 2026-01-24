import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):

    def test_sorting(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, sorted(subjectmarks, key=lambda x: x[1]))

    def test_empty_list(self):
        subjectmarks = []
        result = subject_marks(subjectmarks)
        self.assertEqual(result, [])

    def test_single_element_list(self):
        subjectmarks = [('English', 88)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)

    def test_multiple_elements_list(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        result = subject_marks(subjectmarks)
        self.assertEqual(result, subjectmarks)
