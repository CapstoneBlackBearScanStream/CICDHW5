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
import time
import os
import psutil


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


def quick(int_list):
    """
    qsort docstring
    """
    print("quick sort")


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
