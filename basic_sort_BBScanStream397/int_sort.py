# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers using bubble, quick, and insertion sort and measures resource usage.
"""

from __future__ import annotations
import psutil, time
from typing import List, Tuple


def bubble(int_list: List[int]) -> Tuple[List[int], float]:
    """
    This function uses bubble sort to sort a list of integers and measures CPU percent usage.

    Args:
        int_list List[int]: List of integers to sort.

    Returns:
        sorted_list list[int]: A list containing the sorted integers.
        cpu_usage float: CPU usage as a float.
    """
    data = list(int_list)

    # Initializes CPU measurement to 0
    psutil.cpu_percent(interval=None)

    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    # Measures CPU usage percent since initialization
    cpu_usage = psutil.cpu_percent(interval=0.1)

    return data, cpu_usage


def quick(int_list: List[int]) -> Tuple[List[int], float]:
    """
    This function calls __quickSort__ which is a recursive quicksort algorithm

    Args:
        int_list List[int]: List of integers to sort

    Returns:
        List[int]: the sorted list
        float: the time elapsed from the start and end of sorting in miliseconds
    """
    # Copy the list
    sorted_list = list(int_list)

    # Record the start time
    start_time = time.perf_counter()

    # Call the sorting method
    __quickSort__(sorted_list, 0, len(sorted_list) - 1)

    # Record the end time
    end_time = time.perf_counter()

    # Return the list and time in ms to make it easier to read
    return sorted_list, (end_time - start_time) * 1000


def __quickSort__(int_list: List[int], first: int, last: int):
    if first < last:
        # Create the partition index
        partition_index = __partition__(int_list, first, last)

        # Recursive call
        __quickSort__(int_list, first, partition_index - 1)
        __quickSort__(int_list, partition_index + 1, last)


# This is an implementation of Lomuto Partition
def __partition__(int_list, first, last):
    # Create the pivot at the end
    pivot = int_list[last]

    # Record the first index - 1
    i = first - 1

    # Go through the list element-wise
    for j in range(first, last):
        # If the element is less than the pivot:
        if int_list[j] < pivot:
            # Increase i
            i += 1
            # And swap the elements at i and j
            int_list[i], int_list[j] = int_list[j], int_list[i]

    # Finally, swap the ith + 1 element and the last element in the list
    int_list[i + 1], int_list[last] = int_list[last], int_list[i + 1]
    return i + 1


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
