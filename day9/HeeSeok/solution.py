def solution(numbers, k):
    idx = ((k-1) * 2 ) % len(numbers)
    return numbers[idx]

# Test Cases
print(solution([1, 2, 3, 4], 2))  # 3
print(solution([1, 2, 3, 4, 5, 6], 5))  # 3
print(solution([1, 2, 3], 3))  # 2
