from test_framework import generic_test


# Solution 1: Find and toggle the rightmost 01 or 10 bits
def closest_int_same_bit_count_1(x: int) -> int:
    pass


# Solution 2: Toggle the rightmost 01 or 10 bits in O(1)
def closest_int_same_bit_count_2(x: int) -> int:
    pass


if __name__ == '__main__':
    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_1
    )

    generic_test.generic_test_main(
        'closest_int_same_weight.py',
        'closest_int_same_weight.tsv',
        closest_int_same_bit_count_2
    )
