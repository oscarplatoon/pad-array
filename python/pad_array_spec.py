# Write unit tests!
import unittest
from pad_array import pad

class PadTest(unittest.TestCase):

    def test_type(self):
        self.assertEqual(type(pad([1,2,3],5)),list)

    def test_1(self):
        self.assertEqual(pad([1,2,3],5), [1,2,3,None,None])

    def test_2(self):
        self.assertEqual(pad([1,2,3],5,'apple'), [1,2,3,'apple','apple'])


if __name__ == '__main__':
    unittest.main()