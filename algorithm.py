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

    # Pad strings with space or null character to make equal length
    padded = [s.ljust(max_len) for s in arr]

    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(256)]
        for s in padded:
            ch = s[i]
            buckets[ord(ch)].append(s)
        padded = [s for bucket in buckets for s in bucket]

    # Remove padding before returning
    return [s.rstrip() for s in padded]

