"""
Design a class to calculate the median of a number stream.
The class should have the following two methods:

1. insertNum(int num): stores the number in the class
2. findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will
be the average of the middle two numbers.
"""
import bisect
from collections import deque


class MedianOfAStreamWithHeaps:

    """
    1. store inserted nums in a sorted array
    2. when the median is called:
        1. determine if even or odd numbers
        2. either run avg of 2 middle numbers or return the middle number from odd list
    """

    def __init__(self):
        # if the number of elements is odd, we'll have more numbers in the max heap
        self.max_heap = deque()
        self.min_heap = deque()

    def insert_num(self, num):
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            # insert first number to max heap
            self.max_heap.append(num)
            return

        # 1. check if number is smaller than the last number in the max heap
        if num < self.max_heap[-1]:
            self.max_heap.appendleft(num)
        elif num > self.min_heap[0]:
            self.min_heap.append(num)
        elif num > self.max_heap[-1] and num < self.min_heap[0]:
            # if the value is in-between determine which heap it should go to
            if len(self.min_heap) + 1 <= len(self.max_heap):
                self.min_heap.appendleft(num)
            else:
                self.max_heap.append(num)

        # re-balance heaps
        # max heap at most should be only larger by 1 element
        if len(self.max_heap) > len(self.min_heap) + 1:
            # re-balance heaps
            move_elem = self.max_heap.pop()
            self.min_heap.appendleft(move_elem)
        elif len(self.min_heap) > len(self.max_heap):
            move_elem = self.min_heap.popleft()
            self.max_heap.append(move_elem)

    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + self.max_heap[-1])/2
        else:
            return self.max_heap[-1]


class MedianOfAStreamBisect:

    """
    1. store inserted nums in a sorted array
    2. when the median is called:
        1. determine if even or odd numbers
        2. either run avg of 2 middle numbers or return the middle number from odd list
    """

    def __init__(self):
        self.ordered_list = []

    def insert_num(self, num):
        bisect.insort(self.ordered_list, num)

    def find_median(self):
        len_of_list = len(self.ordered_list)
        is_even = len_of_list % 2 == 0
        if is_even:
            # [1, 4, 5, 7, 8, 9, 12, 13]
            # take average of middle 2 numbers
            index = int(len_of_list / 2)
            result = sum(self.ordered_list[index-1:index+1])/2

            # check if value has zero decimal and return it as an int
            if int(result) == result:
                return int(result)
            else:
                # return the float value
                return result
        else:
            # [1, 4, 5, 7, 8, 9, 12]
            # index out the middle number
            index = int(len_of_list / 2)
            return int(self.ordered_list[index])


def main():
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    median_of_a_stream.insert_num(1)
    assert median_of_a_stream.find_median() == 2
    median_of_a_stream.insert_num(5)
    assert median_of_a_stream.find_median() == 3
    median_of_a_stream.insert_num(4)
    assert median_of_a_stream.find_median() == 3.5


main()
