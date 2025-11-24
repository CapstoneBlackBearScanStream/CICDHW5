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

import pytest
import numpy as np
from basic_sort_BBScanStream397.int_sort import bubble, quick, insertion


def is_sorted(values):
    """
    Testing oracle.
    """
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


@pytest.fixture
def int_lists():
    """
    Testing data for all of the tests.
    """
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5)]


def test_bubble(int_lists):
    """
    Testing for bubble sort. This sorting algorithm should return a sorted list of integers and CPU usage metrics.
    The test asserts that the provided lists are sorted and the the CPU usage percent is 0 or greater.
    The CPU usage percent is then printed.

    Args:
        int_list List[int]: List of integers to sort.

    Returns:
        sorted_list list[int]: A list containing the sorted integers.
        cpu_usage float: CPU usage as a float.
    """
    for lst in int_lists:
        sorted_bubble, cpu_usage = bubble(lst)
        assert is_sorted(sorted_bubble)
        assert cpu_usage >= 0.0
        print(f"CPU Percent: {cpu_usage}")


def test_quick(int_lists):
    """
    Testing for quick sort.

    This method should return a sorted list and the time (in ms) it took for the sorting algorithm.
    This test asserts that the lists are sorted, and the time elapsed is greater than 0.
    The time elapsed is printed.

    Args:
        int_list List[int]: List of integers to sort

    Returns:
        List[int]: the sorted list
        float: the time elapsed from the start and end of sorting in miliseconds
    """

    for lst in int_lists:
        sorted_quick, time = quick(lst)
        assert is_sorted(sorted_quick)
        assert time > 0
        print(f"Time elapsed: {time}")


def test_insertion(int_lists):
    """
    Testing for insertion sort.

    This method should return a sorted list and the memory usage (in MB)
    measured during the sorting algorithm. The test asserts that the
    returned list is sorted and that the measured memory usage is
    non-negative. The memory usage is printed.

    Args:
        int_list List[int]: List of integers to sort

    Returns:
        List[int]: Sorted list
        float: Memory used in MB
    """

    for lst in int_lists:
        sorted_insertion, mem_usage = insertion(lst)
        assert is_sorted(sorted_insertion)
        assert mem_usage >= 0.0
        print(f"Memory used (MB): {mem_usage}")
