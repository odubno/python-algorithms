"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’
sized sub-arrays (or windows) of the array.
"""


class SlidingWindowMedian:
    """
    1. loop over the size of the list
    2. use k to create window of values to consider
    3. sort each window
    4. if number of values in window is odd, pick the middle value,
        otherwise take average of the middle 2 values
    5. store result in list until sliding window is complete
    """

    def __init__(self):

        pass

    def get_median(self, window, k):
        # given list determine the median
        # take median of window
        if k % 2 == 0:
            # take average of center 2 values
            right_value = int(len(window) / 2) + 1
            left_value = int(len(window) / 2) - 1
            median = sum(window[left_value: right_value]) / 2
        else:
            # return the middle value
            middle_index = int(len(window) / 2)
            median = window[middle_index]
        return median

    def find_sliding_window_median(self, nums, k):
        result = []
        # adjust k for 0th index
        adjusted_k = k
        for index in range(len(nums)-k+1):
            # create window range
            start, end = index, adjusted_k
            adjusted_k += 1
            window = nums[start:end]
            # sort window
            window.sort()
            # get median
            median = self.get_median(window, k)
            result.append(median)
        return result


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
