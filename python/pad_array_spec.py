# Write unit tests!
import unittest
from pad_array import pad

class PadTestCase(unittest.TestCase):
    
    #min size equal to list return list
    def test_min_size_equal(self):
        self.assertEqual(pad([1,2,3], 0), [1,2,3])

     #min size less than list return list
    def test_min_size_less(self):
        self.assertEqual(pad([1,2,3], 2), [1,2,3])

    def test_apple(self):
        self.assertEqual(pad([1,2,3], 5, 'apple'), [1,2,3,'apple', 'apple'])

    def test_none(self):
        self.assertEqual(pad([1,2,3], 5), [1,2,3,None,None])

    