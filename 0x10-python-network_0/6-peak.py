#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: A peak integer from the input list. Returns None if the
        list is empty.

    Example:
        >>> find_peak([1, 2, 3, 4, 5])
        5
        >>> find_peak([5, 4, 3, 2, 1])
        5
        >>> find_peak([1, 3, 20, 4, 1, 0])
        20
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
