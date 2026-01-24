import unittest
from mbpp_64_code import str
from collections import namedtuple

from 64_code import subject_marks

SubjectMark = namedtuple('SubjectMark', ['subject', 'mark'])

class TestSubjectMarks(unittest.TestCase):

    def test_sort_normal(self):
        data = [SubjectMark('English', 88), SubjectMark('Science', 90),
                SubjectMark('Maths', 97), SubjectMark('Social sciences', 82)]
        expected = [SubjectMark('Maths', 97), SubjectMark('Science', 90),
                    SubjectMark('English', 88), SubjectMark('Social sciences', 82)]
        self.assertEqual(subject_marks(data), expected)

    def test_sort_edge_cases(self):
        data = [SubjectMark('English', 88), SubjectMark('Science', 90),
                SubjectMark('Maths', 97), SubjectMark('Social sciences', 82),
                SubjectMark('English', 88)]
        expected = [SubjectMark('Maths', 97), SubjectMark('Science', 90),
                    SubjectMark('English', 88), SubjectMark('English', 88),
                    SubjectMark('Social sciences', 82)]
        self.assertEqual(subject_marks(data), expected)

        data = [SubjectMark('English', 88), SubjectMark('Science', 90),
                SubjectMark('Maths', 97), SubjectMark('Social sciences', 82),
                SubjectMark('English', -1)]
        expected = [SubjectMark('Maths', 97), SubjectMark('Science', 90),
                    SubjectMark('English', 88), SubjectMark('English', -1),
                    SubjectMark('Social sciences', 82)]
        self.assertEqual(subject_marks(data), expected)

    def test_sort_invalid_input(self):
        data = [('English', 'invalid'), ('Science', 90), ('Maths', 97),
                ('Social sciences', 82)]
        self.assertRaises(TypeError, subject_marks, data)
