import unittest
from lab1 import *

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

    def test_max(self):
        """Tests a variety of lists containing zeroes, negatives, and positive values, in varying lengths"""
        tlist =  [1, 2, 3, 4, 5, 6, 7, 12]
        tlist2 = [12, 2, 3, 12, 5, 6, 7, 12]
        tlist3 = [12, 4, 5, 6, 7]
        tlist4 = [-7, -4, -1, -6, -7, -12]
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





    def test_rev_rec(self):
        """Tests a number of standard expected lists, including negatives, positives, zeroes, and repeated values."""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([2, 2, 2, 2, 2, 2, 2]), [2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(reverse_rec([0, 1, 6, 2, 4, 6, 0, 21]), [21, 0, 6, 4, 2, 6, 1, 0])
        self.assertEqual(reverse_rec([-3, -5, -8]), [-8, -5, -3])

    def test_rev_rec_empty(self):
        """Reverse function returns the empty list when passed an empty list"""
        self.assertEqual(reverse_rec([]), [])

    def test_rev_rec_none(self):
        """Tests that the recursive return function raises a value error when passed a None-type"""
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_rev_rec_one(self):
        """Should return the same list when passed a list with a single element"""
        self.assertEqual(reverse_rec([9]), [9])




    def test_bin_search_center(self):
        """Tests a search for the initial center value of the list, for both even and odd list lengths"""
        list_val_odd = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_val_even = [1, 5, 6, 7, 8, 11]

        self.assertEqual(bin_search(4, 0, len(list_val_odd)-1, list_val_odd), 4)
        self.assertEqual(bin_search(6, 0, len(list_val_even) - 1, list_val_even), 2)

    def test_bin_search_first(self):
        """Searches for first value in the list, both even and odd list lengths"""
        list_val_odd = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_val_even = [5, 8, 9, 12, 15, 89]
        self.assertEqual(bin_search(0, 0, len(list_val_odd)-1, list_val_odd), 0)
        self.assertEqual(bin_search(5, 0, len(list_val_even) - 1, list_val_even), 0)

    def test_bin_search_last(self):
        """searches for last value the list, for both even and odd list lengths"""
        list_val_odd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14]
        list_val_even = [5, 8, 9, 12, 15, 89]

        self.assertEqual(bin_search(89, 0, len(list_val_even) - 1, list_val_even), 5)
        self.assertEqual(bin_search(14, 0, len(list_val_odd) - 1, list_val_odd), 10)


    def test_bin_search_neg(self):
        """Searches for the target value in a list comprised of negative and mixed-sign numbers, even and odd lengths"""

        list_val_odd_neg = [-19, -17, -13, -11, -7, -5, -3, -2, -1]
        list_val_even_neg = [-12, -11, -5, -4, -2, -1]


        self.assertEqual(bin_search(-13, 0, len(list_val_odd_neg) - 1, list_val_odd_neg), 2)
        self.assertEqual(bin_search(-4, 0, len(list_val_even_neg) - 1, list_val_even_neg), 3)

    def test_bin_search_mixed(self):
        list_val_odd = [-7, -4, 0, 1, 2, 3, 5, 7, 11]
        list_val_even = [-7, -4, 0, 1, 2, 3, 5, 7]

        self.assertEqual(bin_search(0, 0, len(list_val_odd) - 1, list_val_odd), 2)
        self.assertEqual(bin_search(3, 0, len(list_val_even) - 1, list_val_even), 5)

    def test_bin_search_none(self):
        """Tests that the recursive return function raises a value error when passed a None-type"""
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)

    def test_bin_search_empty(self):
        self.assertEqual(bin_search(0, 0, 0, []), None)

    def test_bin_search_missing(self):
        """On even and odd length lists, expects Nonetype if target is absent, both in and out bounds"""
        list_val_odd = [-7, -4, 0, 1, 2, 3, 5, 7, 11]
        list_val_even = [-7, -4, 0, 1, 2, 3, 5, 7]

        self.assertEqual(bin_search(4, 0, len(list_val_odd) - 1, list_val_odd), None)
        self.assertEqual(bin_search(4, 0, len(list_val_even) - 1, list_val_even), None)
        self.assertEqual(bin_search(14, 0, len(list_val_odd) - 1, list_val_odd), None)
        self.assertEqual(bin_search(14, 0, len(list_val_even) - 1, list_val_even), None)
        self.assertEqual(bin_search(-14, 0, len(list_val_odd) - 1, list_val_odd), None)
        self.assertEqual(bin_search(-14, 0, len(list_val_even) - 1, list_val_even), None)


if __name__ == "__main__":
    unittest.main()
