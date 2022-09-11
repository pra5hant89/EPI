RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i];
                break

    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


A = [2, 2, 1, 2, 0, 0, 1, 0, 1, 2, 1, 2, 1, 2, 2, 1]
dutch_flag_partition(2, A)
print(A)
