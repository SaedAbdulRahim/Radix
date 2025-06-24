import streamlit as st
import pandas as pd
import time
import math

def visualize_string_sort(arr):
    st.subheader("🔤 String Radix Sort Visualization")
    if not arr:
        return []

    max_len = max(len(s) for s in arr)
    padded = [s.ljust(max_len) for s in arr]  # pad with spaces

    BUCKETS_PER_DISPLAY = 16  # show 16 buckets per DataFrame for readability
    total_buckets = 256
    num_chunks = math.ceil(total_buckets / BUCKETS_PER_DISPLAY)

    for i in range(max_len - 1, -1, -1):
        st.markdown(f"### Step (char index={i}):")

        buckets = [[] for _ in range(total_buckets)]
        for s in padded:
            index = ord(s[i])
            buckets[index].append(s)

        # Show buckets in chunks of 16
        for chunk in range(num_chunks):
            start = chunk * BUCKETS_PER_DISPLAY
            end = min(start + BUCKETS_PER_DISPLAY, total_buckets)

            # Prepare dict with bucket columns, padding with empty strings
            visible_buckets = {
                f"{chr(b) if 32 <= b <= 126 else b}": pd.Series(buckets[b]) for b in range(start, end)
            }

            max_len_col = max(len(col) for col in visible_buckets.values()) if visible_buckets else 0
            for key in visible_buckets:
                visible_buckets[key] = visible_buckets[key].reindex(range(max_len_col), fill_value="")

            df = pd.DataFrame(visible_buckets)
            st.dataframe(df)

        # Flatten buckets back to list
        padded = [s for bucket in buckets for s in bucket]
        time.sleep(1)

    result = [s.rstrip() for s in padded]
    return result
