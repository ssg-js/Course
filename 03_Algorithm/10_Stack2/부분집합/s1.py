# 부분집합


def powerset(array, depth, total):
    if total > 10:
        return

    if depth == len(numbers):
        if total == 10:
            print(array)
        return
    powerset(array + [numbers[depth]], depth + 1, total + numbers[depth])

    powerset(array, depth + 1, total)


numbers = list(range(1, 11))
powerset([], 0, 0)
