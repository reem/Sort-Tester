 #!/usr/bin/env python
"""
Author: Jonathan Reem
Author email: jonathan.reem@gmail.com
Date: September 2013
Implementation of a comprehensive speed test for sorting algorithms.
 Version 1.0
Prerequisites:
  numpy 1.7.0 or later
    Replace lines 53 and 57 with random.randint calls instead of numpy random
    calls if you don't have it, know this is FAR slower.
Current Features:
  Speed Testing with leaderboard generation over variable size lists
  Options for changing list sizes, number of lists, and others. See docstring
    of sort_test for more info.
  Automatic error detection, and notification along with automatic debug list
    (10 item list) testing for easy debugging.
Future Features:
  Options for pathological data (sorted lists, almost sorted lists,
    lists with high repetition, near reversed lists, etc.)
  Better automatic debugging with pathological data options and more
    helpful errors.
    Where was the problem in the large list? Where they the same length? etc.
"""

import random
import time

try:
    import numpy.random as nprnd
except ImportError:
    def rlist_gen(size, upper_limit):
        "random powered random list generation "
        return [random.randint(0, upper_limit) for _ in xrange(size)]
else:
    def rlist_gen(size, upper_limit):
        "Numpy-powered random list generation."
        return nprnd.randint(upper_limit,
                    size=size).tolist()

def sort_test(sorts_to_test, max_size_order = 7, mult_list_size = True,
                 check_sort = True, verbose_timing = False):
    """
    Takes as input a list of sorts and runs tests on them.
    Set max_size_order to the largest list size you want where the
        size is 10 ** max_size_order. Lengths start at 10 ** 2, so
        the default 7 generates 5 test lists.
    Set mult_list_size to False to check on only one size of list.
        (10 million integers under 100 thousand)
    Set check_sort to False to not do assertions on the sorted lists.
    Set verbose_timing to True to show timing data in real-time.
    """

    unsorted_lists = gen_lists(max_size_order, mult_list_size)
    print ''

    # Gives a notification of progress if verbose timing is turned off.
    if not verbose_timing:
        print "Timing sorts... \n"

    times = {} # sort_name:times_in_order for lookup and use on the leaderboard
    sorted_lists = {} # sort_name:sorted_lists for lookup during sort checking
    for list_num, unsorted in enumerate(unsorted_lists):
        sorted_list = sorted(unsorted)

        # Again, progress indicator.
        if not verbose_timing:
            print "Testing list {}...".format(list_num + 1)

        for sort in sorts_to_test[:]:
            # Copy made here to avoid a nasty bug where the for loop will
            # skip the sort immediately after a broken sort.
            if verbose_timing:
                print "For {} items, trying {}...".format(
                        len(unsorted), sort.__name__)

            #Timing is done inside the try/except blocks to avoid extra time.
            start_time, end_time = 0, 0
            try:
                start_time = time.clock()
                sorted_lists[sort.__name__].append(sort(unsorted))
                end_time = time.clock()
            except KeyError:
                start_time = time.clock()
                sorted_lists[sort.__name__] = list([sort(unsorted)])
                end_time = time.clock()

            try:
                times[sort.__name__].append(end_time - start_time)
            except KeyError:
                times[sort.__name__] = list([end_time - start_time])
            if verbose_timing:
                print "It took: {:.5f}".format(times[sort.__name__][-1])

            if check_sort:
                try:
                    assert sorted_lists[sort.__name__][-1] == sorted_list
                except AssertionError:
                    debug(sort, unsorted)
                    sorts_to_test.remove(sort)
                    print "{} will not be tried again.\n".format(sort.__name__)

    print ''
    gen_leaderboard(unsorted_lists, times, sorts_to_test)

def debug(sort, unsorted):
    """Prints debug information for a failed sort to avoid silent failure and
    removal of the sort."""
    print ''
    print "{} did not work for the random list with {} integers.".format(
        sort.__name__, len(unsorted))

    print "Generating and testing debug list:"
    debug_list = rlist_gen(10, 10)

    print "Initial debug list: ", debug_list
    print "Sorted debug list: ", sorted(debug_list)
    print "Broken sort debug list: ", sort(debug_list)

def gen_leaderboard(unsorted_lists, times, working_sorts):
    """Generates leaderboard from times for the working sorts."""
    for index, unsorted in enumerate(unsorted_lists):
        leaderboard = [(times[sort.__name__][index], sort.__name__)
                for sort in working_sorts]
        leaderboard = sorted(leaderboard)

        print "For list {}, with length {} and range {}: ".format(index + 1,
                len(unsorted), max(unsorted) - min(unsorted) + 1)
        for sort_time, sort_name in leaderboard:
            print "{:.5f} {}".format(sort_time, sort_name)
        print ''

def gen_lists(max_size_order, mult_list_size):
    """Generates random lists for testing."""
    unsorted_lists = []
    if mult_list_size:
        for i in range(2, max_size_order):
            size_random_sample = 10 ** i
            range_upper_limit = 10 ** random.randint(i-1, i)
            print "Generating {} random ints with max size {}...".format(
                    size_random_sample, range_upper_limit)
            random_list = rlist_gen(size_random_sample, range_upper_limit)
            unsorted_lists.append(random_list)
    else:
        size_random_sample = 10 ** max_size_order
        range_upper_limit = 10 ** (max_size_order - 2)
        print "Generating {} random ints with max size {}...".format(
                size_random_sample, range_upper_limit)
        random_list = rlist_gen(size_random_sample, range_upper_limit)
        unsorted_lists.append(random_list)
    return unsorted_lists

def main():
    "Runs sort_test on some sample sorts."
    def bad_sort(unsorted_list):
        "Example of a broken sort"
        return unsorted_list

    def good_sort(unsorted_list):
        "Example of a good sort."
        return sorted(unsorted_list)

    def slow_sort(unsorted_list):
        "Example of a slow sort."
        string_version = ''
        for num in range(len(unsorted_list) // 5):
            string_version += str(num) # Slow operation
        if len(string_version) > len(unsorted_list):
            pass
        return sorted(unsorted_list)

    sort_test([bad_sort, good_sort, slow_sort])

if __name__ == '__main__':
    main()
