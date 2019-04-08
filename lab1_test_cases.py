import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_None(self):
        """Should raise ValueError when passed None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_empty(self):
        """Returns None when passed an empty list"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_std(self):
        """Tests a variety of lists containing zeroes, negatives, and positive values, in varying lengths"""
        tlist =  [1, 2, 3, 4, 5, 6, 7, 12]
        tlist2 = [12, 2, 3, 12, 5, 6, 7, 12]
        tlist3 = [12, 4, 5, 6, 7]
        tlist4 = [-1, -4, -5, -6, -7, -12]
        tlist5 = [-1, 2, -3, -4, 5, -6, 7, -12]
        tlist6 = [2, 4, -3, 0, -9, 0, 2, 4]
        tlist7 = [8]
        tlist8 = [-2, 0, -9, -2]

        self.assertEqual(max_list_iter(tlist), 12)
        self.assertEqual(max_list_iter(tlist2), 12)
        self.assertEqual(max_list_iter(tlist3), 12)
        self.assertEqual(max_list_iter(tlist4), -1)
        self.assertEqual(max_list_iter(tlist5), 7)
        self.assertEqual(max_list_iter(tlist6), 4)
        self.assertEqual(max_list_iter(tlist7), 8)
        self.assertEqual(max_list_iter(tlist8), 0)


#    def test_reverse_rec(self):
#        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
#
#    def test_bin_search(self):
#        list_val =[0,1,2,3,4,7,8,9,10]
#        low = 0
#        high = len(list_val)-1
#        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
    unittest.main()
