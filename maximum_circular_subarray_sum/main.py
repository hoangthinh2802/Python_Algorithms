from typing import List


def get_max_sequence_sum(numbers: List[int], operator = max) -> int:
    result_sequence, sum_sequence = 0, 0 
    for num in numbers:

        sum_sequence = operator(num, sum_sequence + num)
        result_sequence = operator(result_sequence, sum_sequence)
    return result_sequence

def find_max_circular_sequence_num(numbers: List[int]) -> int:
    max_sequence_sum = get_max_sequence_sum(numbers)
    max_wrap_sequence = sum(numbers) - get_max_sequence_sum(numbers, operator = min)
    return max(max_sequence_sum, max_wrap_sequence)


if __name__== '__main__':
    l = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(get_max_sequence_sum(l))
    print(find_max_circular_sequence_num(l))