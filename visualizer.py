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
    st.subheader("🔤 String Radix Sort Visualization")
    if not arr:
        st.warning("Empty input.")
        return []

    max_len = max(len(s) for s in arr)
    step = 1

    for i in range(max_len - 1, -1, -1):
        st.markdown(f"### Step {step}: Sorting by character at position {i}")
        buckets = [[] for _ in range(256)]

        for s in arr:
            char_index = ord(s[i]) if i < len(s) else 0
            buckets[char_index].append(s)

        # Show only non-empty buckets
        display_buckets = {f"{chr(idx) if idx >= 32 and idx < 127 else idx} ({idx})": buckets[idx] 
                           for idx in range(256) if buckets[idx]}
        
        # Find the max bucket length
        max_bucket_len = max(len(lst) for lst in display_buckets.values())
        # Pad each bucket to max length
        padded_buckets = {k: v + [""] * (max_bucket_len - len(v)) for k, v in display_buckets.items()}
        
        bucket_df = pd.DataFrame(padded_buckets)
        st.dataframe(bucket_df)

        arr = [s for bucket in buckets for s in bucket]
        st.success(f"After Step {step}: {arr}")
        time.sleep(1)
        step += 1

    return arr
