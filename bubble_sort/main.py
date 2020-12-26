from typing import List
import random

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__=='__main__':
    nums = [3,4, 6, 14, 13434, 134,4252]
    print(bubble_sort(nums))
    number = [random.randint(1,2344) for i in range(10)]
    print(bubble_sort(number))
    