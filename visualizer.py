import streamlit as st
import time

def visualize_integer_sort(arr):
    st.subheader("Integer Radix Sort Visualization")
    max_num = max(arr) if arr else 0
    exp = 1
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        st.write(f"**Pass (exp={exp}):**", buckets)
        arr = [num for bucket in buckets for num in bucket]
        exp *= 10
        time.sleep(0.5)
    return arr

def visualize_string_sort(arr):
    st.subheader("String Radix Sort Visualization")
    max_len = max(len(s) for s in arr)
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(256)]
        for s in arr:
            index = ord(s[i]) if i < len(s) else 0
            buckets[index].append(s)

        st.write(f"**Pass (char index={i}):**", [b for b in buckets if b])
        arr = [s for bucket in buckets for s in bucket]
        time.sleep(0.5)
    return arr
