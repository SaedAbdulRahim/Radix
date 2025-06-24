import streamlit as st
import pandas as pd
import time

def visualize_integer_sort(arr):
    st.subheader("🔢 Integer Radix Sort Visualization")
    max_num = max(arr) if arr else 0
    exp = 1
    step = 1

    while max_num // exp > 0:
        st.markdown(f"### Step {step}: Sorting by digit at exp = {exp}")
        buckets = [[] for _ in range(10)]

        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        # Visual bucket display
        bucket_df = pd.DataFrame({f'Bucket {i}': pd.Series(buckets[i]) for i in range(10)})
        st.dataframe(bucket_df)

        arr = [num for bucket in buckets for num in bucket]
        st.success(f"After Step {step}: {arr}")
        exp *= 10
        step += 1

        time.sleep(1)
    return arr

def visualize_string_sort(arr):
    st.subheader("String Radix Sort Visualization")
    if not arr:
        return []

    max_len = max(len(s) for s in arr)
    padded = [s.ljust(max_len) for s in arr]  # pad with spaces

    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(256)]
        for s in padded:
            index = ord(s[i])
            buckets[index].append(s)

        # Display only non-empty buckets
        st.write(f"**Pass (char index={i}):**", [bucket for bucket in buckets if bucket])
        time.sleep(0.5)

        padded = [s for bucket in buckets for s in bucket]

    result = [s.rstrip() for s in padded]
    return result
