def radix_sort_integers(arr):
    if not arr:
        return []

    max_length = len(str(max(arr)))
    for digit in range(max_length):
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[(num // 10**digit) % 10].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr

def radix_sort_strings(arr):
    if not arr:
        return []

    max_length = max(len(word) for word in arr)
    for char_index in reversed(range(max_length)):
        buckets = [[] for _ in range(27)]  # 26 letters + 1 for empty/padding
        for word in arr:
            char = word[char_index] if char_index < len(word) else ' '
            index = 0 if char == ' ' else ord(char.lower()) - 96
            buckets[index].append(word)
        arr = [word for bucket in buckets for word in bucket]
    return arr
