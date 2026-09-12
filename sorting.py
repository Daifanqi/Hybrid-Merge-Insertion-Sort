"""
SC2001 Project1 sorting.py
Hybrid merge‑insertion sort, counts key‑comparisons
"""
import sys
sys.setrecursionlimit(10000)


def insertion_sort(arr, lo, hi):
    """
    Sort subarray arr[lo ... hi] in‑place using insertion sort.
    Return: number of key‑comparisons performed.

    lo: start index (inclusive)
    hi: end index (inclusive)
    Every boolean comparison "arr[j] > key" counts as one key‑comparison,
    including the failing comparison that terminates the while‑loop.
    """
    comparisons = 0
    for i in range(lo + 1, hi + 1):
        key = arr[i]
        j = i - 1
        while j >= lo:
            comparisons += 1   # count every element‑to‑element key comparison
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons


def _merge(arr, buf, lo, mid, hi):
    """
    Merge two sorted segments arr[lo~mid] and arr[mid+1~hi].
    buf: shared auxiliary buffer to avoid repeated memory allocation.
    Return: number of key‑comparisons during merge.

    Direct copy of remaining elements does NOT count as key‑comparisons.
    """
    # copy target range into auxiliary buffer
    for k in range(lo, hi + 1):
        buf[k] = arr[k]

    i = lo
    j = mid + 1
    k = lo
    comparisons = 0

    while i <= mid and j <= hi:
        comparisons += 1  # count comparison between left‑side and right‑side element
        if buf[i] <= buf[j]:
            arr[k] = buf[i]
            i += 1
        else:
            arr[k] = buf[j]
            j += 1
        k += 1

    # copy remaining items from left segment, no comparisons
    while i <= mid:
        arr[k] = buf[i]
        i += 1
        k += 1
    # copy remaining items from right segment, no comparisons
    while j <= hi:
        arr[k] = buf[j]
        j += 1
        k += 1
    return comparisons


def _hybrid_sort(arr, buf, lo, hi, S):
    """
    Internal recursive helper function. Do NOT call directly.
    Switch to insertion‑sort when subarray size <= threshold S.
    Return accumulated total key‑comparisons.
    """
    subarray_size = hi - lo + 1
    if subarray_size <= S:
        return insertion_sort(arr, lo, hi)

    mid = (lo + hi) // 2
    comp = 0
    comp += _hybrid_sort(arr, buf, lo, mid, S)
    comp += _hybrid_sort(arr, buf, mid+1, hi, S)
    comp += _merge(arr, buf, lo, mid, hi)
    return comp


def hybrid_sort(arr, S):
    """
    Public entry for hybrid merge‑insertion sort.
    arr: list to sort; will be modified in‑place.
    S: size threshold to switch from merge‑sort to insertion‑sort.
    Return: total number of key‑comparisons.

    When S = 1, hybrid_sort behaves exactly like original merge‑sort.
    """
    n = len(arr)
    if n <= 1:
        return 0
    buf = [0] * n  # allocate auxiliary buffer once per sort call
    return _hybrid_sort(arr, buf, 0, n-1, S)


def merge_sort(arr):
    """
    Original top‑down merge‑sort as taught in lecture.
    Equivalent to hybrid_sort(arr, S=1).
    Return: total number of key‑comparisons.
    """
    return hybrid_sort(arr, S=1)


# ---------------- Self‑test code, runs when executing this file ----------------
if __name__ == "__main__":
    import random
    print("Starting correctness self‑tests...")
    for _ in range(200):
        n = random.randint(0, 50)
        S_test = random.randint(1, 10)
        raw = [random.randint(1, 100) for _ in range(n)]

        a = raw.copy()
        c_hybrid = hybrid_sort(a, S_test)
        assert a == sorted(raw), f"Hybrid sort failed! Input: {raw}"

        b = raw.copy()
        c_original = merge_sort(b)
        assert b == sorted(raw), f"Original merge sort failed! Input: {raw}"

        # S=1 should produce identical comparison count as original merge sort
        c_s1 = hybrid_sort(raw.copy(), S=1)
        assert c_s1 == c_original, "S=1 mismatch: hybrid_sort != merge_sort comparison count"

    print("✅ All self‑tests passed! Algorithm logic is correct.")