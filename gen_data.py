"""
SC2001 Project1 gen_data.py
Dataset generator for sorting experiment
Generate 3 types of arrays: random, sorted ascending, sorted descending
"""
import random


def generate_random_array(n: int) -> list[int]:
    """
    Generate an array of n random integers in range [1, n].
    Return the generated list.
    """
    return [random.randint(1, n) for _ in range(n)]


def generate_ascending_array(n: int) -> list[int]:
    """
    Generate an already sorted array in ascending order.
    """
    return list(range(1, n + 1))


def generate_descending_array(n: int) -> list[int]:
    """
    Generate an array sorted in descending order.
    """
    return list(range(n, 0, -1))


if __name__ == "__main__":
    # Self test for data generator
    print("Test random array: ", generate_random_array(8))
    print("Test ascending array: ", generate_ascending_array(8))
    print("Test descending array: ", generate_descending_array(8))
    print("✅ gen_data self-test done")