def counting_sort(arr, exp, base=10):
    output = [None] * len(arr)
    count = [0] * base

    for num in arr:
        index = (num // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    for num in reversed(arr):
        index = (num // exp) % base
        output[count[index] - 1] = num
        count[index] -= 1

    return output

def radix_sort_integers(arr):
    if not arr:
        return []
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

def radix_sort_strings(arr):
    if not arr:
        return []
    max_len = max(len(s) for s in arr)
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(256)]  # ASCII size
        for s in arr:
            index = ord(s[i]) if i < len(s) else 0
            buckets[index].append(s)
        arr = [s for bucket in buckets for s in bucket]
    return arr
